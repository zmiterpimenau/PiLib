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

from reference_book.views import show_author_list, show_author_by_pk, show_serie_list, show_serie_by_pk, show_genre_by_pk, show_genre_list, show_publisher_by_pk, show_publisher_list, show_ref_books

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/<int:author_id>/', show_author_by_pk),
    path('author/', show_author_list),
    path('serie/<int:serie_id>/', show_serie_by_pk),
    path('serie/', show_serie_list),
    path('genre/<int:genre_id>/', show_genre_by_pk),
    path('genre/', show_genre_list),
    path('publisher/<int:publisher_id>/', show_publisher_by_pk),
    path('publisher/', show_publisher_list),
    path('', show_ref_books),
]
