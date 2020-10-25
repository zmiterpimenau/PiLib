# Generated by Django 3.1.2 on 2020-10-25 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
        ('books', '0016_auto_20201025_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_genre',
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='book', to='reference_book.genre', verbose_name='Жанры'),
            preserve_default=False,
        ),
    ]
