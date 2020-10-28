from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Serie, Genre, Publisher
from books.models import Book

def show_author_list(request):
    """Return list of Author objects"""
    authors = Author.objects.all()
    con = {"authors_key": authors}
    return render(request, template_name="refs/author_list.html", context=con)

def show_author_by_pk(request, author_id):
    """Return list of Author profile"""
    author_obj = Author.objects.get(pk=author_id)
    book_obj = author_obj.book.all()
    con = {"author_key": author_obj, "book_key": book_obj}
    return render(request, template_name="refs/author.html", context=con)

def show_serie_list(request):
    """Return list of Serie objects"""
    series = Serie.objects.all()
    con = {"series_key": series}
    return render(request, template_name="refs/serie_list.html", context=con)

def show_serie_by_pk(request, serie_id):
    """Return list of Author profile"""
    serie_obj = Serie.objects.get(pk=serie_id)
    book_obj = serie_obj.book.all()
    con = {"serie_key": serie_obj, "book_key": book_obj}
    return render(request, template_name="refs/serie.html", context=con)

def show_genre_list(request):
    """Return list of Genre objects"""
    genres = Genre.objects.all()
    con = {"genres_key": genres}
    return render(request, template_name="refs/genre_list.html", context=con)

def show_genre_by_pk(request, genre_id):
    """Return list of Genre profile"""
    genre_obj = Genre.objects.get(pk=genre_id)
    book_obj = genre_obj.book.all()
    con = {"genre_key": genre_obj, "book_key": book_obj}
    return render(request, template_name="refs/genre.html", context=con)

def show_publisher_list(request):
    """Return list of Genre objects"""
    publishers = Publisher.objects.all()
    con = {"publishers_key": publishers}
    return render(request, template_name="refs/publisher_list.html", context=con)

def show_publisher_by_pk(request, publisher_id):
    """Return list of Genre profile"""
    publisher_obj = Publisher.objects.get(pk=publisher_id)
    book_obj = publisher_obj.book.all()
    con = {"publisher_key": publisher_obj, "book_key": book_obj}
    return render(request, template_name="refs/publisher.html", context=con)

def show_ref_books(request):
    """Return list of all reference books"""
    return render(request, template_name="refs/refs.html")