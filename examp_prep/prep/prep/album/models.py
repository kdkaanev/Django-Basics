from django.core.validators import MinValueValidator
from django.db import models

from prep.user_profile.models import Profile

# Create your models here.
class Genre(models.TextChoices):
    POP = "Pop Music"
    JAZZ = "Jazz Music"
    ROCK = "Rock Music"
    HIPHOP = "Hip Hop Music"
    RNB = "R&B Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    OTHER = "Other"

MIN_PRICE = 0.0

class Album(models.Model):
    album_name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        verbose_name='Artist',

    )
    genre = models.CharField(
        max_length=30,
        choices=Genre.choices,
        null=False,
        blank=False,
        verbose_name='Genre',
    )

    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image Url',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE, 'Ensure this value is greater than or equal to 0.0'),

        ),
        verbose_name='Price',
    )
    #hidden field in form
    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
    )
