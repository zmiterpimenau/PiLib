from django.urls import path
from django.views.generic.base import View

from . import views

app_name = 'orders'
urlpatterns = [
    #path('add/', views.AddProducrToCartView.as_view(), name='add_product'),
    path('delete-book-in-cart/<int:pk>', views.DeleteBookInCart.as_view(), name='book-in-cart-del'),
    path('update-cart', views.CartUpdateView.as_view(), name='cart-update'),
    path('', views.CartView.as_view(), name='cart')
]
