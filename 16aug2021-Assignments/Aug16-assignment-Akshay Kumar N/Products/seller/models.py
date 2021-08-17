from django.db import models

class Sellers(models.Model): 
    sellerid = models.IntegerField()
    sellername = models.CharField(max_length=50)
    selleraddress = models.CharField(max_length=50)
    sellerphno = models.CharField(max_length=50)

