from pyexpat import model
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.
class Signup(models.Model):
   
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)
    balance = models.IntegerField()
  
    

    def __str__(self):
     return self.fname



# class Login(models.Model):
#     fname = models.CharField(max_length=100)
#     passs = models.CharField(max_length=100)


