# Generated by Django 3.1.2 on 2020-11-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='series',
            field=models.CharField(max_length=50, verbose_name='Название серии'),
        ),
    ]
