from django.db import models
from reference_book.models import Author, Serie, Genre, Publisher

class Book(models.Model):
    book_name = models.CharField(
        'Название книги',
        max_length=100
    )
    book_description = models.TextField(
        'Описание книги',
        blank=True,
        null=True
    )

    book_price = models.DecimalField(
        'Цена книги',
        default=0.0,
        max_digits=10,
        decimal_places=2
    )

    book_year = models.CharField(
        'Год издания',
        max_length=4
    )

    book_pages = models.CharField(
        'Количество страниц',
        max_length=5
    )

    COVER_CHOICES = [
        ('hard', 'Твердая обложка'),
        ('soft', 'Мягкая обложка'),
        ('sup', 'Суперобложка'),
        ('halfsoft', 'Полумягкая обложка'),
        ('cloth', 'Тканевая обложка'),
        ('unknown', 'Не указано')
    ]
    book_cover = models.CharField(
        'Вид обложки',
        max_length=50,
        default='unknown',
        choices=COVER_CHOICES
    )

    book_isbn = models.CharField(
        'ISBN',
        max_length=20
    )

    book_weight = models.CharField(
        'Вес в граммах',
        max_length=5
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
