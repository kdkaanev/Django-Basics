# Generated by Django 5.0.2 on 2024-02-20 05:50

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2, 'Ensure this value is at least 2 characters long.')])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Pop', 'Pop Music'), ('Jazz', 'Jazz Music'), ('Rock', 'Rock Music'), ('Hiphop', 'Hip Hop Music'), ('R&B', 'R&B Music'), ('Country', 'Country Music'), ('Dance', 'Dance Music'), ('Other', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Ensure this value is greater than or equal to 0.0')])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.profile')),
            ],
        ),
    ]