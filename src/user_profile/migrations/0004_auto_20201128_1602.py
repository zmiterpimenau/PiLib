# Generated by Django 3.1.2 on 2020-11-28 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_auto_20201128_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]
