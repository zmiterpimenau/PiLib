# Generated by Django 3.1.2 on 2020-10-24 17:57

from django.db import migrations, models

 
class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20201024_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_availability',
            field=models.CharField(default=0, max_length=6, verbose_name='Количество книг в наличии'),
        ),
    ]
