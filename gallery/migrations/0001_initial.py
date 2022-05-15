# Generated by Django 4.0.4 on 2022-05-14 15:09

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('alt', models.CharField(blank=True, max_length=200)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]