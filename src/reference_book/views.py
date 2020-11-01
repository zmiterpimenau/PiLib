from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Author, Serie, Genre, Publisher
from books import models


from .forms import CreateGenreForm, UpdateGenreForm, CreateAuthorForm, UpdateAuthorForm, CreateSerieForm, UpdateSerieForm, CreatePublisherForm, UpdatePublisherForm

def show_author_list_view(request):
    """Return list of Author objects"""
    authors = Author.objects.all()
    con = {"authors_key": authors}
    return render(request, template_name="refs/author_list.html", context=con)

def show_author_by_pk_view(request, author_id):
    """Return list of Author profile"""
    author_obj = Author.objects.get(pk=author_id)
    book_obj = author_obj.book.all()
    con = {"author_key": author_obj, "book_key": book_obj}
    return render(request, template_name="refs/author.html", context=con)

def create_author_view(request):
    if request.method == 'POST':
        form = CreateAuthorForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get('author')
            Author.objects.create(author=author_name)
            return HttpResponseRedirect('/')
    else:
        form = CreateAuthorForm()
    header = 'Создать автора'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def update_author_view(request, author_id):
    if request.method == 'POST':
        form = UpdateAuthorForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get('author')
            form_pk = form.cleaned_data.get('author_id')
            obj = Author.objects.get(pk=form_pk)
            obj.author=author_name
            obj.save()
            return HttpResponseRedirect('/')
    else:
        author = Author.objects.get(pk=author_id)
        form = UpdateAuthorForm(data={'author': author.author, 'author_id': author.pk})
    header = 'Обновить автора'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def delete_author_view(request, author_id):
    if request.method == 'POST':
        Author.objects.get(pk=author_id).delete()
        return HttpResponseRedirect('/')
    else:
        obj = Author.objects.get(pk=author_id)
    header = 'Удалить автора'
    return render(
        request, 
        template_name="refs/delete_object.html", 
        context={'obj': obj, 'header': header})

def show_serie_list_view(request):
    """Return list of Serie objects"""
    series = Serie.objects.all()
    con = {"series_key": series}
    return render(request, template_name="refs/serie_list.html", context=con)

def show_serie_by_pk_view(request, serie_id):
    """Return list of Author profile"""
    serie_obj = Serie.objects.get(pk=serie_id)
    book_obj = serie_obj.book.all()
    con = {"serie_key": serie_obj, "book_key": book_obj}
    return render(request, template_name="refs/serie.html", context=con)

def create_serie_view(request):
    if request.method == 'POST':
        form = CreateSerieForm(data=request.POST)
        if form.is_valid():
            serie_name = form.cleaned_data.get('series')
            Serie.objects.create(series=serie_name)
            return HttpResponseRedirect('/')
    else:
        form = CreateSerieForm()
    header = 'Создать новую серию'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def update_serie_view(request, serie_id):
    if request.method == 'POST':
        form = UpdateSerieForm(data=request.POST)
        if form.is_valid():
            serie_name = form.cleaned_data.get('series')
            form_pk = form.cleaned_data.get('serie_id')
            obj = Serie.objects.get(pk=form_pk)
            obj.series=serie_name
            obj.save()
            return HttpResponseRedirect('/')
    else:
        serie = Serie.objects.get(pk=serie_id)
        print(serie.series)
        form = UpdateSerieForm(data={'series': serie.series, 'serie_id': serie.pk})
    header = 'Обновить серию'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def delete_serie_view(request, serie_id):
    if request.method == 'POST':
        Serie.objects.get(pk=serie_id).delete()
        return HttpResponseRedirect('/')
    else:
        obj = Serie.objects.get(pk=serie_id)
    header = 'Удалить серию'
    return render(
        request, 
        template_name="refs/delete_object.html", 
        context={'obj': obj, 'header': header})

def show_genre_list_view(request):
    """Return list of Genre objects"""
    genres = Genre.objects.all()
    con = {"genres_key": genres}
    return render(request, template_name="refs/genre_list.html", context=con)

def show_genre_by_pk_view(request, genre_id):
    """Return list of Genre profile"""
    genre_obj = Genre.objects.get(pk=genre_id)
    book_obj = genre_obj.book.all()
    con = {"genre_key": genre_obj, "book_key": book_obj}
    return render(request, template_name="refs/genre.html", context=con)

def create_genre_view(request):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            genre_name = form.cleaned_data.get('genres')
            Genre.objects.create(genres=genre_name)
            return HttpResponseRedirect('/')
    else:
        form = CreateGenreForm()
    header = 'Создать жанр'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def update_genre_view(request, genre_id):
    if request.method == 'POST':
        form = UpdateGenreForm(data=request.POST)
        if form.is_valid():
            genre_name = form.cleaned_data.get('genres')
            form_pk = form.cleaned_data.get('genre_id')
            obj = Genre.objects.get(pk=form_pk)
            obj.genres=genre_name
            obj.save()
            return HttpResponseRedirect('/')
    else:
        genre = Genre.objects.get(pk=genre_id)
        form = UpdateGenreForm(data={'genres': genre.genres, 'genre_id': genre.pk})
    header = 'Обновить жанр'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def delete_genre_view(request, genre_id):
    if request.method == 'POST':
        Genre.objects.get(pk=genre_id).delete()
        return HttpResponseRedirect('/')
    else:
        obj = Genre.objects.get(pk=genre_id)
    header = 'Удалить жанр'
    return render(
        request, 
        template_name="refs/delete_object.html", 
        context={'obj': obj, 'header': header})

def show_publisher_list_view(request):
    """Return list of Genre objects"""
    publishers = Publisher.objects.all()
    con = {"publishers_key": publishers}
    return render(request, template_name="refs/publisher_list.html", context=con)

def show_publisher_by_pk_view(request, publisher_id):
    """Return list of Genre profile"""
    publisher_obj = Publisher.objects.get(pk=publisher_id)
    book_obj = publisher_obj.book.all()
    con = {"publisher_key": publisher_obj, "book_key": book_obj}
    return render(request, template_name="refs/publisher.html", context=con)

def create_publisher_view(request):
    if request.method == 'POST':
        form = CreatePublisherForm(data=request.POST)
        if form.is_valid():
            publisher_name = form.cleaned_data.get('publisher')
            Publisher.objects.create(publisher=publisher_name)
            return HttpResponseRedirect('/')
    else:
        form = CreatePublisherForm()
    header = 'Создать издателя'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def update_publisher_view(request, publisher_id):
    if request.method == 'POST':
        form = UpdatePublisherForm(data=request.POST)
        if form.is_valid():
            publisher_name = form.cleaned_data.get('publisher')
            form_pk = form.cleaned_data.get('publisher_id')
            obj = Publisher.objects.get(pk=form_pk)
            obj.publisher=publisher_name
            obj.save()
            return HttpResponseRedirect('/')
    else:
        publisher = Publisher.objects.get(pk=publisher_id)
        form = UpdatePublisherForm(data={'publisher': publisher.publisher, 'publisher_id': publisher.pk})
    header = 'Обновить издателя'
    return render(
        request, 
        template_name="refs/create_object.html", 
        context={'form': form, 'header': header}
        )

def delete_publisher_view(request, publisher_id):
    if request.method == 'POST':
        Publisher.objects.get(pk=publisher_id).delete()
        return HttpResponseRedirect('/')
    else:
        obj = Publisher.objects.get(pk=publisher_id)
    header = 'Удалить издателя'
    return render(
        request, 
        template_name="refs/delete_object.html", 
        context={'obj': obj, 'header': header})

def show_ref_books_view(request):
    """Return list of all reference books"""
    return render(request, template_name="refs/refs.html")