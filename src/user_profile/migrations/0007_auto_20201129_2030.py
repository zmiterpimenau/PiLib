# Generated by Django 3.1.2 on 2020-11-29 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20201129_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='second_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Второй адрес'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='third_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Третий адрес'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.IntegerField(blank=True, max_length=50, null=True, verbose_name='Индекс'),
        ),
    ]
