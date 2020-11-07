from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Author, Serie, Genre, Publisher
from books import models

from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView, DetailView

from .forms import CreateGenreForm, UpdateGenreForm, CreateAuthorForm, UpdateAuthorForm, CreateSerieForm, UpdateSerieForm, CreatePublisherForm, UpdatePublisherForm

class ShowRefBooksView(TemplateView):
    template_name = "refs/refs.html"

class ShowAuthorListView(ListView):
    template_name = 'refs/refbook_list.html'
    model = Author
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Список авторов"
        context["link"] = "/author/create"
        context["obj_name"] = "author"
        context["header"] = "Создать нового автора"
        return context
"""    
    def get_queryset(self):
        return super().get_queryset()
"""
    
class CreateAuthorView(CreateView):
    model = Author
    form_class = CreateAuthorForm
    success_url = '/author'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Создать автора"
        return context
    
class UpdateAuthorView(UpdateView):
    model = Author
    form_class = UpdateAuthorForm
    success_url = '/author'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить карточку автора"
        return context

class DeleteAuthorView(DeleteView):
    model = Author
    success_url = '/author'
    template_name = 'refs/delete_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить автора"
        return context       

class ShowAuthorByPKView(DetailView):
    template_name = "refs/author.html"
    model = Author
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Author.objects.get(pk=key)
        context["book_list"] = Author.objects.get(pk=key).book.all()
        return context
    
class ShowSerieListView(ListView):
    template_name = 'refs/refbook_list.html'
    model = Serie
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Список серий"
        context["link"] = "/serie/create"
        context["obj_name"] = "serie"
        context["header"] = "Создать новую серию"
        return context

class CreateSerieView(CreateView):
    model = Serie
    form_class = CreateSerieForm
    success_url = '/serie'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Создать серию"
        return context
    
class UpdateSerieView(UpdateView):
    model = Serie
    form_class = UpdateSerieForm
    success_url = '/serie'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить данные серии"
        return context

class DeleteSerieView(DeleteView):
    model = Serie
    success_url = '/serie'
    template_name = 'refs/delete_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить серию"
        return context       

class ShowSerieByPKView(DetailView):
    template_name = "refs/serie.html"
    model = Serie
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Serie.objects.get(pk=key)
        context["book_list"] = Serie.objects.get(pk=key).book.all()
        return context
    
class ShowGenreListView(ListView):
    template_name = 'refs/refbook_list.html'
    model = Genre
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Список жанров"
        context["link"] = "/genre/create"
        context["obj_name"] = "genre"
        context["header"] = "Создать карточку нового жанра"
        return context

class CreateGenreView(CreateView):
    model = Genre
    form_class = CreateGenreForm
    success_url = '/genre'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Добавить жанр"
        return context
    
class UpdateGenreView(UpdateView):
    model = Genre
    form_class = UpdateGenreForm
    success_url = '/genre'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить данные жанра"
        return context

class DeleteGenreView(DeleteView):
    model = Genre
    success_url = '/genre'
    template_name = 'refs/delete_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить жанр"
        return context       

class ShowGenreByPKView(DetailView):
    template_name = "refs/genre.html"
    model = Genre
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Genre.objects.get(pk=key)
        context["book_list"] = Genre.objects.get(pk=key).book.all()
        return context

class ShowPublishereListView(ListView):
    template_name = 'refs/refbook_list.html'
    model = Publisher
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Список издательств"
        context["link"] = "/publisher/create"
        context["obj_name"] = "publisher"
        context["header"] = "Создать карточку нового издательства"
        return context

class CreatePublisherView(CreateView):
    model = Publisher
    form_class = CreatePublisherForm
    success_url = '/publisher'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Добавить издателя"
        return context
    
class UpdatePublisherView(UpdateView):
    model = Publisher
    form_class = UpdatePublisherForm
    success_url = '/publisher'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить данные издательства"
        return context

class DeletePublisherView(DeleteView):
    model = Publisher
    success_url = '/publisher'
    template_name = 'refs/delete_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить издательство"
        return context       

class ShowPublisherByPKView(DetailView):
    template_name = "refs/publisher.html"
    model = Publisher
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Publisher.objects.get(pk=key)
        context["book_list"] = Publisher.objects.get(pk=key).book.all()
        return context