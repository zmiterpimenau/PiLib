# Generated by Django 3.1.2 on 2020-10-24 17:52

from django.db import migrations, models
 
 
class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_book_book_restrictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_restrictions',
            field=models.CharField(choices=[('no_restriction', '0+'), ('underthree', '3+'), ('undersix', '6+'), ('underten', '10+'), ('undersixteen', '16+'), ('adultonly', '18+')], default='no_restriction', max_length=50, verbose_name='Возрастные ограничения'),
        ),
    ]
