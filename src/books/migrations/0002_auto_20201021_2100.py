# Generated by Django 3.1.2 on 2020-10-21 18:00

from django.db import migrations, models
import django.db.models.deletion

 

class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_serie',
        ),
        migrations.AddField(
            model_name='book',
            name='book_serie',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='reference_book.serie', verbose_name='Серия книги'),
            preserve_default=False,
        ),
    ]
