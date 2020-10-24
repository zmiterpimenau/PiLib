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

    RESTRICTIONS = [
        ('no_restriction', '0+'),
        ('underthree', '3+'),
        ('undersix', '6+'),
        ('underten', '10+'),
        ('undersixteen', '16+'),
        ('adultonly', '18+')
    ]

    book_restrictions = models.CharField(
        'Возрастные ограничения',
        max_length=50,
        default='no_restriction',
        choices=RESTRICTIONS
    )

    book_quantity = models.IntegerField(
        'Количество книг в наличии',
        default=0
    )

    AVAILABLE = [
        ('yes', 'Доступен для заказа'),
        ('no', 'Нет в наличии')
    ]
    
    book_availability = models.CharField(
        'Статус книги',
        max_length=20,
        default='no',
        choices=AVAILABLE
    )

    RATING = []
    for i in range(11):
        var = (str(i), i)
        RATING.append(var)

    book_rating = models.IntegerField(
        'Рейтинг книги',
        default='0',
        choices=RATING
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
        related_name='Книга'
    )
    
    book_serie = models.ForeignKey(
        Serie,
        verbose_name='Серия книги',
        on_delete=models.PROTECT,
        related_name='Книга'
    )
    
    book_genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='Книга'
    )
    
    book_publisher = models.ForeignKey(
        Publisher,
        verbose_name='Издательство',
        on_delete=models.PROTECT,
        related_name='Книга'
    )

    def __str__(self):
        return f'{self.book_name} {self.book_adding_date}'
