"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from hello_world.views import hello_world

from reference_book import views
from books import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/create/', views.CreateAuthorView.as_view()),
    path('author/update/<int:pk>/', views.UpdateAuthorView.as_view()),
    path('author/', views.ShowAuthorListView.as_view()),
    path('author/delete/<int:pk>/', views.DeleteAuthorView.as_view()),
    path('author/<int:pk>/', views.ShowAuthorByPKView.as_view()),
    path('serie/create/', views.CreateSerieView.as_view()),
    path('serie/update/<int:pk>/', views.UpdateSerieView.as_view()),
    path('serie/delete/<int:pk>/', views.DeleteSerieView.as_view()),
    path('serie/<int:pk>/', views.ShowSerieByPKView.as_view()),
    path('serie/', views.ShowSerieListView.as_view()),
    path('genre/', views.ShowGenreListView.as_view()),
    path('genre/create/', views.CreateGenreView.as_view()),
    path('genre/update/<int:pk>/', views.UpdateGenreView.as_view()),
    path('genre/delete/<int:pk>/', views.DeleteGenreView.as_view()),
    path('genre/<int:pk>/', views.ShowGenreByPKView.as_view()),
    path('publisher/<int:pk>/', views.ShowPublisherByPKView.as_view()),
    path('publisher/', views.ShowPublishereListView.as_view()),
    path('publisher/create/', views.CreatePublisherView.as_view()),
    path('publisher/update/<int:pk>/', views.UpdatePublisherView.as_view()),
    path('publisher/delete/<int:pk>/', views.DeletePublisherView.as_view()),
    path('book/<int:pk>/', v.ShowBookByPKView.as_view()),
    path('book/', v.ShowBookListView.as_view()),
    path('book/create/', v.CreateBookView.as_view()),
    path('book/update/<int:pk>/', v.UpdateBookView.as_view()),
    path('book/delete/<int:pk>/', v.DeleteBookView.as_view()),
    path('', views.ShowRefBooksView.as_view()),
]
