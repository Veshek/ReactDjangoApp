from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    # null (database related ) = True allows the data to be stored as null in the database
    # blank (validation related ) = True allows forms to be submitted with this field as an empty value
    # null and blank are typically used together as the form will allow empty values and the database will
    # store that value as null 
    age = models.PositiveIntegerField(null=True, blank=True)
    happiness = models.PositiveIntegerField(null=True, blank=True)

