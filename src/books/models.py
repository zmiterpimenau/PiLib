from django.db import models
from reference_book.models import Author, Serie, Genre, Publisher

class BookCover(models.Model):
    book_cover = models.CharField(
        'Вид обложки',
        max_length=50
    )

    def __str__(self):
        return f'{self.book_cover}'

class BookRestrictions(models.Model):
    book_restrictions = models.CharField(
        'Возрастные ограничения',
        max_length=50
    )

    def __str__(self):
        return f'{self.book_restrictions}'

class BookAvailability(models.Model):
    book_availability = models.CharField(
        'Доступность книги',
        max_length=50
    )

    def __str__(self):
        return f'{self.book_availability}'

class BookRating(models.Model):
    book_rating = models.CharField(
        'Рейтинг книги',
        max_length=50
    )

    def __str__(self):
        return f'{self.book_rating}'

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
        'Цена книги(BYN)',
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

    book_cover = models.ForeignKey(
        BookCover,
        verbose_name='Вид обложки',
        on_delete=models.PROTECT,
        related_name='bookcover'
    )

    book_isbn = models.CharField(
        'ISBN',
        max_length=20
    )

    book_weight = models.CharField(
        'Вес в граммах',
        max_length=5
    )

    book_restrictions = models.ForeignKey(
        BookRestrictions,
        verbose_name='Возрастные ограничения',
        on_delete=models.PROTECT,
        related_name='bookrestrictions'
    )

    book_quantity = models.IntegerField(
        'Количество книг в наличии',
        default=0
    )
    
    book_availability = models.ForeignKey(
        BookAvailability,
        verbose_name='Доступность книги',
        on_delete=models.PROTECT,
        related_name='bookavailability'
    )

    book_rating = models.ForeignKey(
        BookRating,
        verbose_name='Рейтинг книги',
        on_delete=models.PROTECT,
        related_name='bookrating'
    )

    book_adding_date = models.DateField(
        verbose_name='Дата внесения в каталог',
        auto_now=False,
        auto_now_add=True
    )

    book_updating_date = models.DateTimeField(
        verbose_name='Дата последнего изменения карточки',
        auto_now=True,
        auto_now_add=False
    )
    
    book_author = models.ManyToManyField(
        Author,
        verbose_name='Автор книги',
        related_name='book'
    )
    
    book_serie = models.ForeignKey(
        Serie,
        verbose_name='Серия книги',
        on_delete=models.PROTECT,
        related_name='book'
    )
    
    book_genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='book'
    )
    
    book_publisher = models.ForeignKey(
        Publisher,
        verbose_name='Издательство',
        on_delete=models.PROTECT,
        related_name='book'
    )

    def __str__(self):
        return f'{self.book_name}'
