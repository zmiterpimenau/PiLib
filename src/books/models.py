from django.db import models
from reference_book.models import Author, Serie, Genre, Publisher

class Book(models.Model):
    book_name = models.CharField(
        'Название книги',
        max_length=100,
        blank=False,
        null=False,
    )
    book_description = models.TextField(
        'Описание книги',
        blank=True,
        null=True
    )
    
    book_author = models.ManyToManyField(
        Author,
        verbose_name='Автор книги'
    )
    
    book_serie = models.ForeignKey(
        Serie,
        verbose_name='Серия книги',
        on_delete=models.PROTECT
    )
    
    book_genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанры'
    )
    
    book_publisher = models.ForeignKey(
        Publisher,
        verbose_name='Издательство',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.book_name
