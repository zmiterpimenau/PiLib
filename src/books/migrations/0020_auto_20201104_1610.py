# Generated by Django 3.1.2 on 2020-11-04 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0019_auto_20201026_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookCover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_cover', models.CharField(max_length=50, verbose_name='Вид обложки')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookcover', to='books.bookcover', verbose_name='Вид обложки'),
        ),
    ]
