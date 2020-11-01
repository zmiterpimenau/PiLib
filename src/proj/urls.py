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
    path('author/<int:author_id>/', views.show_author_by_pk_view),
    path('author/', views.show_author_list_view),
    path('author/create/', views.create_author_view),
    path('author/update/<int:author_id>/', views.update_author_view),
    path('author/delete/<int:author_id>/', views.delete_author_view),
    path('serie/<int:serie_id>/', views.show_serie_by_pk_view),
    path('serie/', views.show_serie_list_view),
    path('serie/create/', views.create_serie_view),
    path('serie/update/<int:serie_id>/', views.update_serie_view),
    path('serie/delete/<int:serie_id>/', views.delete_serie_view),
    path('book/<int:book_id>/', v.show_book_by_pk_view),
    path('book/', v.show_book_list_view),
    path('book/create/', v.create_book_view),
    path('book/update/<int:book_id>/', v.update_book_view),
    path('book/delete/<int:book_id>/', v.delete_book_view),
    path('genre/<int:genre_id>/', views.show_genre_by_pk_view),
    path('genre/', views.show_genre_list_view),
    path('genre/create/', views.create_genre_view),
    path('genre/update/<int:genre_id>/', views.update_genre_view),
    path('genre/delete/<int:genre_id>/', views.delete_genre_view),
    path('publisher/<int:publisher_id>/', views.show_publisher_by_pk_view),
    path('publisher/', views.show_publisher_list_view),
    path('publisher/create/', views.create_publisher_view),
    path('publisher/update/<int:publisher_id>/', views.update_publisher_view),
    path('publisher/delete/<int:publisher_id>/', views.delete_publisher_view),
    path('', views.show_ref_books_view),
]
