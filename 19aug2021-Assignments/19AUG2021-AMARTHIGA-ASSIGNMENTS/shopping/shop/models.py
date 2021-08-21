from django.db import models

# Create your models here.
class shops(models.Model):
    shopname = models.CharField(max_length=50, default = '')
    shopadd = models.CharField(max_length=50, default = '')
    website = models.CharField(max_length=50, default = '')
    phone = models.BigIntegerField(default='')
    username = models.CharField(max_length=50, default = '')
    password = models.CharField(max_length=50, default = '')
    confirmpass = models.CharField(max_length=50, default = '')
