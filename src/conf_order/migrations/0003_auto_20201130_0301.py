# Generated by Django 3.1.2 on 2020-11-30 00:01

from django.db import migrations, models

 
class Migration(migrations.Migration):

    dependencies = [
        ('conf_order', '0002_auto_20201130_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, choices=[('The order is being processed', 'The order is being processed'), ('The order is being delivered', 'The order is being delivered'), ('The order was canceled', 'The order was canceled'), ('The order is completed', 'The order is completed')], max_length=100, null=True, verbose_name='Статус заказа'),
        ),
    ]