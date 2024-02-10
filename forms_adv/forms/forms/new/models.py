from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models import DO_NOTHING

from forms.new import validators
# Create your models here.
class Person(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(3),
            validators.validate_name,

        ]
    )
    age = models.IntegerField()
    email = models.EmailField()
    prifile_image = models.ImageField(
        upload_to='profile_images',
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        User, on_delete=DO_NOTHING,
        null=True,
        blank=True
    )