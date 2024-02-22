# Generated by Django 5.0.2 on 2024-02-22 16:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Album Name'),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=30, verbose_name='Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Pop', 'Pop Music'), ('Jazz', 'Jazz Music'), ('Rock', 'Rock Music'), ('Hiphop', 'Hip Hop Music'), ('R&B', 'R&B Music'), ('Country', 'Country Music'), ('Dance', 'Dance Music'), ('Other', 'Other')], max_length=30, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='album',
            name='image_url',
            field=models.URLField(verbose_name='Image Url'),
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Ensure this value is greater than or equal to 0.0')], verbose_name='Price'),
        ),
    ]