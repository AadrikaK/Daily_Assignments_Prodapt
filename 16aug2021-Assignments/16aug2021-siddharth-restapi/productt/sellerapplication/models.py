from django.db import models

class Seller(models.Model):
    sname=models.CharField(max_length=50)
    sid=models.IntegerField()
    sadd=models.CharField(max_length=50)
    sphone=models.CharField(max_length=50)
