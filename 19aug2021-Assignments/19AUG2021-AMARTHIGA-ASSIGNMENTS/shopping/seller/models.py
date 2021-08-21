from django.db import models

# Create your models here.
class sellers(models.Model):
    sellername = models.CharField(max_length=50, default = '')
    address = models.CharField(max_length=50, default = '')
    email = models.CharField(max_length=50, default = '')
    phone = models.BigIntegerField(default = '')
    dateofbirth= models.DateField(default = '')
    age = models.IntegerField( default = '')
    aadhar = models.IntegerField(default='')