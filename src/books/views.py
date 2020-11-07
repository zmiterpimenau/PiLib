from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView, DetailView

from .models import Book
from .forms import CreateBookForm, UpdateBookForm
from reference_book.models import Author, Genre, Serie, Publisher

class CreateBookView(CreateView):
    model = Book
    form_class = CreateBookForm
    success_url = '/book'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Создать книгу"
        return context
    
class UpdateBookView(UpdateView):
    model = Book
    form_class = UpdateBookForm
    success_url = '/book'
    template_name = 'refs/create_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Обновить карточку книги"
        return context

class DeleteBookView(DeleteView):
    model = Book
    success_url = '/book'
    template_name = 'refs/delete_object.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header"] = "Удалить книгу"
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
    template_name = 'refs/refbook_list.html'
    model = Book
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Список книг"
        context["link"] = "/book/create"
        context["obj_name"] = "book"
        context["header"] = "Создать новую книгу"
        return context


