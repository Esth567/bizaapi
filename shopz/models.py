from django.db import models
from django.contrib .auth.models import User
import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=60)



class Products(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.CharField('Category', max_length=200)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) 

  
    def __str__(self):
        return self.name
      
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

class Stores(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null = True, db_constraint=False)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    manufacturer = models.CharField('Manufacturer', max_length=200,)   
    products = models.CharField('Products' ,max_length=200,  default='')
    category = models.CharField('Category' ,max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)
    description =  models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True) 
