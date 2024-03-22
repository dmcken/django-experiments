'''Core models'''
from django.db import models

# Create your models here.
class Package(models.Model):
    '''Package model.
    '''
    name = models.CharField(max_length=200)

class Customer(models.Model):
    '''Customer model.
    '''
    name = models.CharField(max_length=200)



class Service(models.Model):
    '''Service model.
    '''
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    package  = models.ForeignKey(Package,  on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)
