# Generated by Django 4.2.2 on 2023-06-19 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrendingItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.brand'),
        ),
        migrations.AddField(
            model_name='item',
            name='trending_items_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop_app.trendingitemcategory'),
        ),
    ]
