# Generated by Django 3.1.2 on 2020-10-24 18:09

from django.db import migrations, models
 
 
class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20201024_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_quantity',
            field=models.IntegerField(default=0, verbose_name='Количество книг в наличии'),
        ),
    ]
