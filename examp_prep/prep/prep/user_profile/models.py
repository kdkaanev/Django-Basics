from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MinLengthValidator




# Create your models here.

MIN_LENGTH_USERNAME = 2

class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(
            MinLengthValidator(MIN_LENGTH_USERNAME, 'Ensure this value is at least 2 characters long.'),
        ),
        null=False,
        blank=False,

    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,

    )


