# Generated by Django 4.0.4 on 2022-05-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='alt',
            field=models.CharField(max_length=200),
        ),
    ]