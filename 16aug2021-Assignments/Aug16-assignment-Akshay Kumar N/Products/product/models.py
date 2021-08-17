from django.db import models

class Products(models.Model):  #Creating collections for storing data in database
    prodcode = models.IntegerField()
    prodname = models.CharField(max_length=50)
    proddesc = models.CharField(max_length=50)
    prodprice = models.IntegerField()

