# Generated by Django 3.1.2 on 2020-11-04 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0020_auto_20201104_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_availability', models.CharField(max_length=50, verbose_name='Доступность книги')),
            ],
        ),
        migrations.CreateModel(
            name='BookRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_rating', models.CharField(max_length=50, verbose_name='Рейтинг книги')),
            ],
        ),
        migrations.CreateModel(
            name='BookRestrictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_restrictions', models.CharField(max_length=50, verbose_name='Возрастные ограничения')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_availability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookavailability', to='books.bookavailability', verbose_name='Доступность книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookrating', to='books.bookrating', verbose_name='Рейтинг книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_restrictions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookrestrictions', to='books.bookrestrictions', verbose_name='Возрастные ограничения'),
        ),
    ]
