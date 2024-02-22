from django.core.validators import MinValueValidator
from django.db import models

from prep.user_profile.models import Profile

# Create your models here.

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
        choices=CHOICES_GENRE,
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
