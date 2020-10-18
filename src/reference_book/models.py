from django.db import models

class Author(models.Model):
    author = models.CharField(
        'Имя автора',
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.author

class Serie(models.Model):
    series = models.CharField(
        'Номер серии',
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.series

class Genre(models.Model):
    genres = models.CharField(
        'Жанр книги',
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.genres

class Publisher(models.Model):
    publisher = models.CharField(
        'Издательство',
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.publisher