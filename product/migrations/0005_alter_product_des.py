# Generated by Django 4.0.5 on 2022-07-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.CharField(max_length=500),
        ),
    ]
