# Generated by Django 4.2.1 on 2023-06-24 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_alter_item_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='targe_customer',
            new_name='target_customer',
        ),
    ]