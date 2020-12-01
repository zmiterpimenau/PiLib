# Generated by Django 3.1.2 on 2020-10-24 19:00

from django.db import migrations, models
import django.db.models.deletion
 
 
class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
        ('books', '0013_auto_20201024_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.ManyToManyField(related_name='Книга', to='reference_book.Author', verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_genre',
            field=models.ManyToManyField(related_name='Книга', to='reference_book.Genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Книга', to='reference_book.publisher', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Книга', to='reference_book.serie', verbose_name='Серия книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_updating_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения карточки'),
        ),
    ]
