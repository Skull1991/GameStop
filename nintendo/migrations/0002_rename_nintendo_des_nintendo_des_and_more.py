# Generated by Django 4.0.5 on 2022-07-08 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nintendo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nintendo',
            old_name='nintendo_des',
            new_name='des',
        ),
        migrations.RenameField(
            model_name='nintendo',
            old_name='nintendo_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='nintendo',
            old_name='nintendo_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='nintendo',
            old_name='nintendo_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='nintendo',
            old_name='nintendo_quantity',
            new_name='quantity',
        ),
    ]
