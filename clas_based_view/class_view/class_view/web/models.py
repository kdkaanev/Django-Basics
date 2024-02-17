from django.db import models
from django.template.defaultfilters import slugify
import uuid


def get_random_hash():
    return uuid.uuid4().hex[:4]


# Create your models here.
class Todo(models.Model):
    MAX_TITLE_LENGTH = 24
    MAX_TENANT_LENGTH = 24
    description = models.TextField()
    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False
    )

    slug = models.SlugField(
        editable=False,
        default='asd'
    )

    tenant = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        null=True,
        blank=True,
        default=None,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + get_random_hash()
        return super().save(*args, **kwargs)
