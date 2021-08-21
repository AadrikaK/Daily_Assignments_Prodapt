from django.db import models

# Create your models here.
class products(models.Model):
    proname = models.CharField(max_length=50, default = '')
    prodetail = models.CharField(max_length=50, default = '')
    seller = models.CharField(max_length=50, default = '')
    manufacturer = models.CharField(max_length=50, default = '')
    manudate= models.DateField(default = '')
    expirydate = models.DateField( default = '')
    price = models.IntegerField(default='')
    