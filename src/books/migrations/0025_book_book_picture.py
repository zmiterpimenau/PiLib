# Generated by Django 3.1.2 on 2020-11-15 12:47

import books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0024_auto_20201108_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_picture',
            field=models.ImageField(default='file.txt', upload_to=books.models.upload, verbose_name='Изображение обложки'),
            preserve_default=False,
        ),
    ]