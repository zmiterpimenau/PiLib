from django.urls import path
from django.views.generic.base import View


from . import views

app_name = 'orders'
urlpatterns = [
    path('delete-book-in-cart/<int:pk>', views.DeleteBookInCart.as_view(), name='book-in-cart-del'),
    path('update-cart', views.CartUpdateView.as_view(), name='cart-update'),
    path('', views.CartView.as_view(), name='cart')
]
