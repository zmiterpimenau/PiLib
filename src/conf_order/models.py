from django.db import models
from orders.models import Cart

class Order(models.Model):
    cart = models.OneToOneField(
        Cart,
        on_delete=models.PROTECT
    )

    status = models.BooleanField(
        'Отменить заказ',
        default=False
    )

    order_status = models.CharField(
        'Статус заказа',
        choices=(('В обработке', 'В обработке'),('Доставка', 'Доставка'), ('Отменен', 'Отменен'),('Выполнен', 'Выполнен')),
        max_length=100,
        default = 'В обработке',
    )

    delivery_address = models.CharField(
        'Адрес доставки',
        max_length=100
    )

    phone = models.CharField(
        'Номер телефона',
        max_length=15
    )

    additional_info = models.CharField(
        'Дополнительная информация',
        max_length=150,
        blank=True,
        null=True
    )

    adding_date = models.DateTimeField(
        verbose_name='Время создания заказа',
        auto_now=False,
        auto_now_add=True
    )

    updating_date = models.DateTimeField(
        verbose_name='Время последнего изменения заказа',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return f"Номер заказа: {self.pk}"
    
