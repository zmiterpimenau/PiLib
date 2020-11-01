from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Book
from .forms import CreateBookForm, UpdateBookForm
from reference_book.models import Author, Genre, Serie, Publisher

def show_book_list_view(request):
    """Return list of Author objects"""
    books = Book.objects.all()
    con = {"books_key": books}
    return render(request, template_name="books/book_list.html", context=con)

def show_book_by_pk_view(request, book_id):
    """Return list of Author profile"""
    book_obj = Book.objects.get(pk=book_id)
    author_obj = book_obj.book_author.all()
    genre_obj = book_obj.book_genre.all()
    con = {"book_obj": book_obj, "author_obj": author_obj, "genre_obj": genre_obj}
    return render(request, template_name="books/book.html", context=con)

def create_book_view(request):
    if request.method == 'POST':
        form = CreateBookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = CreateBookForm()
    header = 'Создать книгу'
    return render(
        request, 
        template_name="books/create_book.html", 
        context={'form': form, 'header': header})

def update_book_view(request, book_id):
    if request.method == 'POST':
        form = UpdateBookForm(data=request.POST)
        if form.is_valid():
            form.save()
            book = Book.objects.get(pk=book_id).delete()
            return HttpResponseRedirect('/')
    else:
        book = Book.objects.get(pk=book_id)
        form = UpdateBookForm(data={
            'book_id': book.pk, 
            'book_name': book.book_name, 
            'book_description': book.book_description,
            'book_price': book.book_price,
            'book_year': book.book_year,
            'book_pages': book.book_pages,
            'book_cover': book.book_cover,
            'book_isbn': book.book_isbn,
            'book_weight': book.book_weight,
            'book_restrictions': book.book_restrictions,
            'book_quantity': book.book_quantity,
            'book_availability': book.book_availability,
            'book_rating': book.book_rating,
            'book_author': book.book_author.all(), 
            'book_genre': book.book_genre.all(),
            'book_serie': book.book_serie,
            'book_publisher': book.book_publisher
            })
    header = 'Обновить книгу'
    return render(
        request, 
        template_name="books/create_book.html",
        context={'form': form, 'header': header}
        )

def delete_book_view(request, book_id):
    if request.method == 'POST':
        Book.objects.get(pk=book_id).delete()
        return HttpResponseRedirect('/')
    else:
        obj = Book.objects.get(pk=book_id)
    header = 'Удалить книгу'
    return render(
        request, 
        template_name="books/delete_book.html",
        context={'obj': obj, 'header': header, 'book': obj.book_name})
