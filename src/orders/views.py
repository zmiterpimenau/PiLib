from django.views.generic import TemplateView, DeleteView, RedirectView
from orders import models
from books import models as book_models
from django.urls import reverse_lazy

def create_cart(user, session):
    cart = models.Cart.objects.create(customer=user)
    session['cart_id'] = cart.pk
    return cart

class CartView(TemplateView):
    template_name='orders/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        cart_id = self.request.session.get('cart_id')
        user = self.request.user

        if not isinstance(user, models.User):
            user = None
            
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = create_cart(user, self.request.session)
        else:
            cart = create_cart(user, self.request.session)
        context["cart"] = cart

       
        # add a book to the cart
        # check input
        book_id = self.request.GET.get('book')
        if not book_id:
            return context
        book = book_models.Book.objects.filter(pk=int(book_id)).first()
        if book:        
            book_in_cart, created = models.ProductInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity': 1,
                    'price': book.book_price
                }
            )
            if not created:
                book_in_cart.quantity = book_in_cart.quantity + 1
                book_in_cart.price = book_in_cart.construct_price()
                book_in_cart.save()  
        else:
            pass # some redirect
        
        context["book"] = book
       
        return context

"""
class AddProducrToCartView(TemplateView):
    template_name = 'orders/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if not isinstance(user, models.User):
            user = None
        
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
            if not cart:
                cart = create_cart(user, self.request.session)
        else:
            cart = create_cart(user, self.request.session)
        
        book_id = self.request.GET.get('book')
        book = book_models.Book.objects.filter(pk=book_id).first()

        if book:
            book_in_cart, created = models.ProductInCart.objects.get_or_create(
                book=book,
                cart=cart,
                defaults={
                    'quantity': 1,
                    'price': book.book_price
                }
            )

            if not created:
                book_in_cart.quantity = book_in_cart.quantity + 1
                book_in_cart.price = book_in_cart.construct_price()
                book_in_cart.save()

        context["cart"] = cart
        context["book"] = book

        return context
"""
    

class DeleteBookInCart(DeleteView):
    model = models.ProductInCart
    template_name='orders/delete-book-in-cart.html'
    success_url = reverse_lazy('orders:cart')

class CartUpdateView(RedirectView):
    def get_redirect_url(self):
        cart_id = self.request.session.get('cart_id')
        user = self.request.user
        if cart_id:
            cart = models.Cart.objects.filter(pk=cart_id).first()
        else:
            # redirect to error page
            pass
        button = self.request.POST.get('submit_button')
        if button == 'edit':
            obj_list = []
            for book_in_cart_id, quantity in self.request.POST.items():
                if book_in_cart_id not in ['csrfmiddlewaretoken', 'submit_button']:
                    # some check needed
                    book_in_cart = models.ProductInCart.objects.get(pk=int(book_in_cart_id))
                    if book_in_cart.cart.pk == cart_id:
                        book_in_cart.quantity = int(quantity)
                        obj_list.append(book_in_cart)
            models.ProductInCart.objects.bulk_update(obj_list, ['quantity'])
        else:
            pass
            # checkout

    
        return reverse_lazy('orders:cart')


