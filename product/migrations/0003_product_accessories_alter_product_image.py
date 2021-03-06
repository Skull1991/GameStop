# Generated by Django 4.0.5 on 2022-07-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_category_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='accessories',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='static/images/home'),
        ),
    ]
