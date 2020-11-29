from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        related_name='profile'
        )

    first_name = models.CharField(
        'Имя',
        max_length=50,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        'Фамилия',
        max_length=50,
        blank=True,
        null=True
    )

    password = models.CharField(
        'Пароль',
        max_length=50
    )

    email = models.EmailField(
        'Email',
        max_length=50
    )

    phone_number = models.CharField(
        verbose_name='Номер телефона', 
        max_length=20
    )

    country = models.CharField(
        verbose_name='Страна', 
        max_length=100, 
        blank=True,
        null=True
    )

    city = models.CharField(
        verbose_name='Город', 
        max_length=50, 
        blank=True,
        null=True
    )

    zip_code = models.IntegerField(
        'Индекс', 
        blank=True,
        null=True
    )

    second_address = models.CharField(
        'Второй адрес', 
        max_length=100, 
        blank=True,
        null=True
    )

    third_address = models.CharField(
        'Третий адрес', 
        max_length=100, 
        blank=True,
        null=True
    )

    additional_information = models.CharField(
        'Дополнительная информация',
        max_length=200,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        create = UserProfile.objects.create(user=instance)
        create.save()