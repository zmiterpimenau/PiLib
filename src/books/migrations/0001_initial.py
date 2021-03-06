# Generated by Django 3.1.2 on 2020-10-20 22:00

from django.db import migrations, models

 

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100, verbose_name='Название книги')),
                ('book_description', models.TextField(blank=True, null=True, verbose_name='Описание книги')),
                ('book_author', models.ManyToManyField(to='reference_book.Author', verbose_name='Автор книги')),
                ('book_genre', models.ManyToManyField(to='reference_book.Genre', verbose_name='Жанры')),
                ('book_publisher', models.ManyToManyField(to='reference_book.Publisher', verbose_name='Издательство')),
                ('book_serie', models.ManyToManyField(to='reference_book.Serie', verbose_name='Серия книги')),
            ],
        ),
    ]
