# Generated by Django 3.1.2 on 2020-11-29 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0004_productincart_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Отменить заказ')),
                ('order_status', models.CharField(choices=[('The order is being processed', 'The order is being processed'), ('The order is being delivered', 'The order is being delivered'), ('The order was canceled', 'The order was canceled'), ('The order is completed', 'The order is completed')], max_length=100, verbose_name='Статус заказа')),
                ('delivery_address', models.CharField(max_length=100, verbose_name='Адрес доставки')),
                ('phone', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('additional_info', models.CharField(blank=True, max_length=150, null=True, verbose_name='Дополнительная информация')),
                ('adding_date', models.DateTimeField(auto_now_add=True, verbose_name='Время создания заказа')),
                ('updating_date', models.DateTimeField(auto_now=True, verbose_name='Время последнего изменения заказа')),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='orders.cart')),
            ],
        ),
    ]
