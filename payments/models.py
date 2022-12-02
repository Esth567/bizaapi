from django.db import models
from django.contrib .auth.models import User



# Create your models here.

class Payment(models.Model):
    name = models.CharField(("name"), max_length=50, default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    password = models.CharField(("password"), max_length=50, default=1)
    phone_number = models.CharField(max_length=30, default=1)
    account_balance = models.CharField(max_length=15, default=0.0)
    account_number = models.CharField(max_length=30, null=True)
    registered_date = models.BooleanField(default=False)
    amount = models.FloatField(max_length=15, default=0.0)
    updated_date = models.DateTimeField(blank=True, default=True)
    