# Generated by Django 4.0.5 on 2022-07-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='playstation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('des', models.CharField(max_length=255)),
                ('image', models.FileField(default='default.jpg', upload_to='static/images/playstation')),
            ],
            options={
                'db_table': 'playstation',
            },
        ),
    ]
