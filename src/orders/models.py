from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='carts',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        "Created date", 
        auto_now=False, 
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        "Updated date",
        auto_now=True,
        auto_now_add=False
    )

    def total_price(self):
        price = 0
        for book_in_cart in self.products.all():
            price += book_in_cart.price
        return price


class ProductInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="products"
    )
    book = models.ForeignKey(
        'books.Book',
        on_delete=models.PROTECT,
        related_name='books_in_carts'
    )
    quantity = models.IntegerField(
        "Количество",
        default=1
    )
    price = models.DecimalField(
        "Цена",
        decimal_places=2,
        max_digits=7
    )

    def __str__(self):
        return f"{self.book.book_name} in cart for {self.cart.customer.username}"
    
    def construct_price(self):
        return self.quantity * self.book.book_price

