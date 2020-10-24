# Generated by Django 3.1.2 on 2020-10-24 18:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20201024_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_adding_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата внесения в каталог'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_updating_date',
            field=models.DateField(auto_now=True, verbose_name='Дата последнего изменения карточки'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_availability',
            field=models.CharField(choices=[(0, 'Доступен для заказа'), (1, 'Нет в наличии')], default=1, max_length=20, verbose_name='Статус книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_quantity',
            field=models.IntegerField(default=0, max_length=10, verbose_name='Количество книг в наличии'),
        ),
    ]
