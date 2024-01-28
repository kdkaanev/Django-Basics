from django.db import models
def non_empty_space(value):
    if " " in value:
        raise ValueError("Spaces are not allowed")
# Create your models here.


class Department(models.Model):
    name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
    )
    def __str__(self):
        return self.name
class Employee(models.Model):

    ROLES = [
        (1, 'Software Developer'),
        (2, 'Manager'),

    ]
    first_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
        validators=[non_empty_space],
    )
    last_name = models.CharField(
        max_length=35,
        blank=False,
        null=False,
    )
    role = models.IntegerField(
       choices=ROLES,
   )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True
    )
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"