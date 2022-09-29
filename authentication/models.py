from pyexpat import model
from statistics import mode
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    password = models.CharField(max_length=65, min_length=8, write_only=True)
    email = models.EmailField(max_length=255, min_length=4)
    first_name = models.CharField(max_length=255, min_length=2)
    last_name = models.CharField(max_length=255, min_length=2)

    def __str__(self):
        return self.email


# Create your models here.
