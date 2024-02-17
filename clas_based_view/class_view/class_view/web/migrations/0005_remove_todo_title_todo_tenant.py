# Generated by Django 5.0.2 on 2024-02-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_todo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='tenant',
            field=models.CharField(blank=True, default=None, max_length=24, null=True),
        ),
    ]