from django.db import models


class Courier(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=50)
    cdeladdress = models.CharField(max_length=50)
    cpincode = models.IntegerField()
    
