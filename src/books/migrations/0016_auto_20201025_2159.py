# Generated by Django 3.1.2 on 2020-10-25 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
        ('books', '0015_auto_20201025_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_author',
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='reference_book.author', verbose_name='Автор книги'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_genre',
            field=models.ManyToManyField(related_name='book', to='reference_book.Genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book', to='reference_book.publisher', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_rating',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, verbose_name='Рейтинг книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_serie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book', to='reference_book.serie', verbose_name='Серия книги'),
        ),
    ]