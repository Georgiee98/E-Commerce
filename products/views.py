from django.shortcuts import render
from .models import  Product
# Create your views here.

def save(self, *args, **kwargs):
    self.datetime_field = self.datetime_field.replace(tzinfo=None)
    super(Product, self).save(*args, **kwargs)