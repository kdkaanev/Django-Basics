# Generated by Django 5.0.1 on 2024-01-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0002_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.IntegerField(choices=[(1, 'Software Developer'), (2, 'Manager')]),
        ),
    ]