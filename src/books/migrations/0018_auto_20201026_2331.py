# Generated by Django 3.1.2 on 2020-10-26 20:31

from django.db import migrations, models
 
 
class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
        ('books', '0017_auto_20201025_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_author',
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.ManyToManyField(related_name='book', to='reference_book.Author', verbose_name='Автор книги'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_genre',
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ManyToManyField(related_name='book', to='reference_book.Genre', verbose_name='Жанры'),
        ),
    ]
