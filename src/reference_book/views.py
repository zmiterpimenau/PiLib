from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Author, Serie, Genre, Publisher
from books.models import *

from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView, DetailView

from .forms import CreateGenreForm, UpdateGenreForm, CreateAuthorForm, UpdateAuthorForm, CreateSerieForm, UpdateSerieForm, CreatePublisherForm, UpdatePublisherForm

class ShowRefBooksView(TemplateView):
    template_name = "refs/main.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        l = len(Book.objects.all()) - 10
        context["new_books"] = Book.objects.order_by('book_adding_date')[l:]
        context["top_books"] = Book.objects.order_by('book_rating')[l:]
        return context
    

class ShowAuthorListView(ListView):
    template_name = 'refs/author_list.html'
    paginate_by = 10
    model = Author
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = "Создать автора"
        context["header"] = "Список авторов"
        return context
    
class CreateAuthorView(LoginRequiredMixin, CreateView):
    model = Author
    form_class = CreateAuthorForm
    success_url = '/author'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Создать автора"
        return context
    
class UpdateAuthorView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = UpdateAuthorForm
    success_url = '/author'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить карточку автора"
        return context

class DeleteAuthorView(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = '/author'
    template_name = 'refs/delete_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get(self.pk_url_kwarg)
        context["header"] = "Удалить автора"
        context["obj"] = Author.objects.get(pk=key)
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
    template_name = 'refs/serie_list.html'
    model = Serie
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = "Создать новую серию"
        context["header"] = "Список серий"
        return context

class CreateSerieView(LoginRequiredMixin, CreateView):
    model = Serie
    form_class = CreateSerieForm
    success_url = '/serie'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Создать серию"
        return context
    
class UpdateSerieView(LoginRequiredMixin, UpdateView):
    model = Serie
    form_class = UpdateSerieForm
    success_url = '/serie'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить данные серии"
        return context

class DeleteSerieView(LoginRequiredMixin, DeleteView):
    model = Serie
    success_url = '/serie'
    template_name = 'refs/delete_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить серию"
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Serie.objects.get(pk=key)
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
    template_name = 'refs/genre_list.html'
    model = Genre
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = "Создать карточку нового жанра"
        context["header"] = "Список жанров"
        return context

class CreateGenreView(LoginRequiredMixin, CreateView):
    model = Genre
    form_class = CreateGenreForm
    success_url = '/genre'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Добавить жанр"
        return context
    
class UpdateGenreView(LoginRequiredMixin, UpdateView):
    model = Genre
    form_class = UpdateGenreForm
    success_url = '/genre'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить данные жанра"
        return context

class DeleteGenreView(LoginRequiredMixin, DeleteView):
    model = Genre
    success_url = '/genre'
    template_name = 'refs/delete_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить жанр"
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Genre.objects.get(pk=key)
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
    template_name = 'refs/publisher_list.html'
    model = Publisher
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Список издательств"
        context["task"] = "Создать карточку нового издательства"
        return context

class CreatePublisherView(LoginRequiredMixin, CreateView):
    model = Publisher
    form_class = CreatePublisherForm
    success_url = '/publisher'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Добавить издателя"
        return context
    
class UpdatePublisherView(LoginRequiredMixin, UpdateView):
    model = Publisher
    form_class = UpdatePublisherForm
    success_url = '/publisher'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить данные издательства"
        return context

class DeletePublisherView(LoginRequiredMixin, DeleteView):
    model = Publisher
    success_url = '/publisher'
    template_name = 'refs/delete_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить издательство"
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Publisher.objects.get(pk=key)
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