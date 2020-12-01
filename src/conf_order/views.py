from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages as msg

from conf_order.models import Order
from user_profile.models import UserProfile
from orders.models import Cart, ProductInCart
from books.models import Book, BookAvailability

class CreateOrderView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name= 'orders/buy_goods.html'
    model = Order
    fields = ('delivery_address', 'phone', 'additional_info')
    login_url = reverse_lazy('login')

    def get_object(self, *args, **kwargs):
        user = self.request.user
        user_profile = UserProfile.objects.get(user=user)

        cart_id = self.request.session.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        order_id = self.request.session.get('order_id')

        book_in_cart = ProductInCart.objects.all().filter(cart_id=cart_id)

        for book in book_in_cart:
            current_book = Book.objects.filter(pk=book.book.pk).last()

            new_count = current_book.book_quantity - book.quantity
            if new_count >= 0:
                current_book.book_quantity = new_count
            else:
                book.quantity = current_book.book_quantity
                book.delete()
            current_book.save()

            if current_book.book_quantity == 0:
                current_book.book_availability = BookAvailability.objects.all().last()
                current_book.save()

        book_in_cart_new = ProductInCart.objects.all().filter(cart=cart_id)
        if len(book_in_cart_new) == 0:
            return None


        order = Order.objects.create(cart=cart)
        self.request.session['order_id'] = order.pk

        if user_profile.second_address:
            order.delivery_address = user_profile.second_address
        if user_profile.phone_number:
            order.phone = user_profile.phone_number
            order.save()
        del self.request.session['cart_id']
        return order

    def get_success_url(self):
        del self.request.session['order_id']
        return reverse_lazy('profile:user_profile')

    def get_success_message(self, cleaned_data):
        return f"{self.object}  - оформлен. Ожидайте звонка нашего специалиста."

