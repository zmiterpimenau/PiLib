# Generated by Django 3.1.2 on 2020-10-26 20:57

from django.db import migrations, models
import django.db.models.deletion
  

class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
        ('books', '0018_auto_20201026_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_genre',
            field=models.ManyToManyField(blank=True, null=True, related_name='book', to='reference_book.Genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='reference_book.publisher', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_serie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='reference_book.serie', verbose_name='Серия книги'),
        ),
    ]
