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
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from hello_world.views import hello_world

from reference_book import views
from reference_book import auth_view
from books import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/create/', views.CreateAuthorView.as_view(), name='author-create'),
    path('author/update/<int:pk>/', views.UpdateAuthorView.as_view(), name='author-update'),
    path('author/', views.ShowAuthorListView.as_view()),
    path('author/delete/<int:pk>/', views.DeleteAuthorView.as_view(), name='author-delete'),
    path('author/<int:pk>/', views.ShowAuthorByPKView.as_view(), name='author-view'),
    path('serie/create/', views.CreateSerieView.as_view(), name='serie-create'),
    path('serie/update/<int:pk>/', views.UpdateSerieView.as_view(), name='serie-update'),
    path('serie/delete/<int:pk>/', views.DeleteSerieView.as_view(), name='serie-delete'),
    path('serie/<int:pk>/', views.ShowSerieByPKView.as_view(), name='serie-view'),
    path('serie/', views.ShowSerieListView.as_view()),
    path('genre/', views.ShowGenreListView.as_view()),
    path('genre/create/', views.CreateGenreView.as_view(), name='genre-create'),
    path('genre/update/<int:pk>/', views.UpdateGenreView.as_view(), name='genre-update'),
    path('genre/delete/<int:pk>/', views.DeleteGenreView.as_view(), name='genre-delete'),
    path('genre/<int:pk>/', views.ShowGenreByPKView.as_view(), name='genre-view'),
    path('publisher/<int:pk>/', views.ShowPublisherByPKView.as_view(), name='publisher-view'),
    path('publisher/', views.ShowPublishereListView.as_view()),
    path('publisher/create/', views.CreatePublisherView.as_view(), name='publisher-create'),
    path('publisher/update/<int:pk>/', views.UpdatePublisherView.as_view(), name='publisher-update'),
    path('publisher/delete/<int:pk>/', views.DeletePublisherView.as_view(), name='publisher-delete'),
    path('book/<int:pk>/', v.ShowBookByPKView.as_view(), name='book-view'),
    path('book/', v.ShowBookListView.as_view()),
    path('book/create/', v.CreateBookView.as_view(), name="book-create"),
    path('book/update/<int:pk>/', v.UpdateBookView.as_view(), name='book-update'),
    path('book/delete/<int:pk>/', v.DeleteBookView.as_view(), name='book-delete'),
    path('auth_login/', auth_view.MyLoginView.as_view(), name= 'login'),
    path('', views.ShowRefBooksView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
