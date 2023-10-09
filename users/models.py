from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    zip_code = models.PositiveIntegerField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

