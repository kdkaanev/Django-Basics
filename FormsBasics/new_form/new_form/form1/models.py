from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
    )
