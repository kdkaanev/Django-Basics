# Generated by Django 5.0.2 on 2024-02-14 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_todo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield9e5e', editable=False),
        ),
    ]
