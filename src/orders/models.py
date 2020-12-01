from django.db import models
from django.contrib.auth.models import User
from user_profile.models import UserProfile
from books.models import Book

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='carts',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(
        "Дата внесения в каталог", 
        auto_now=False, 
        auto_now_add=True
    )
    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False
    )

    def total_price(self):
        price = 0
        for book_in_cart in self.products.all():
            price += book_in_cart.price
        return price

    def __str__(self):
        return f"Корзина #{self.pk}"


class ProductInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="products"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='books_in_cart'
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

    @property
    def construct_price(self):
        price = self.quantity * self.book.book_price
        if price == 0:
            return 0
        return price

    def __str__(self):
        return f'Книга "{self.book.book_name}" в корзине #{self.cart.pk}, количество - {self.quantity}'
    class Meta:
        unique_together = (('cart', 'book'),)
    

