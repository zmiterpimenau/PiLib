# Generated by Django 3.1.2 on 2020-10-24 18:55

from django.db import migrations, models
 
 
class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20201024_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_rating',
            field=models.IntegerField(choices=[('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], default='0', verbose_name='Рейтинг книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Цена книги(BYN)'),
        ),
    ]
