from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MinLengthValidator




# Create your models here.

MIN_LENGTH_USERNAME = 2
MIN_PRICE = 0.0
CHOICES_GENRE = (
    ("Pop", "Pop Music"),
    ("Jazz", "Jazz Music"),
    ("Rock", "Rock Music"),
    ("Hiphop", "Hip Hop Music"),
    ("R&B", "R&B Music"),
    ("Country", "Country Music"),
    ("Dance", "Dance Music"),
    ("Other", "Other"),
)
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

    )


class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
    )
    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,

    )
    genre = models.CharField(
        max_length=30,
        choices=CHOICES_GENRE,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE, 'Ensure this value is greater than or equal to 0.0'),

        )
    )
    #hidden field in form
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
