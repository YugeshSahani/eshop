# Generated by Django 4.2.1 on 2023-06-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_cartitems_total_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='cart_total_price',
            field=models.FloatField(default=0),
        ),
    ]
