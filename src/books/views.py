from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book
from .forms import CreateBookForm, UpdateBookForm
from reference_book.models import Author, Genre, Serie, Publisher

class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = CreateBookForm
    success_url = '/book'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Создать книгу"
        return context
    
class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = UpdateBookForm
    success_url = '/book'
    template_name = 'refs/create_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить карточку книги"
        return context

class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/book'
    template_name = 'refs/delete_object.html'
    login_url = '/auth_login'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить книгу"
        key = self.kwargs.get(self.pk_url_kwarg)
        context["obj"] = Book.objects.get(pk=key)
        return context       

class ShowBookByPKView(DetailView):
    template_name = "refs/book.html"
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        key = self.kwargs.get(self.pk_url_kwarg)
        some_book = Book.objects.get(pk=key)
        context["book_obj"] = some_book
        context["author_obj"] = some_book.book_author.all()
        context["genre_obj"] = some_book.book_genre.all()
        return context

class ShowBookListView(ListView):
    template_name = 'refs/book_list.html'
    paginate_by = 10
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Список книг"
        return context


