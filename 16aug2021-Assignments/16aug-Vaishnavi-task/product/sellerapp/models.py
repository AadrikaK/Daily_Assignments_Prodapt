from django.db import models

# Create your models here.
class sellersdata(models.Model):
    seller_name = models.CharField(max_length=50)
    seller_id = models.IntegerField()
    seller_address =models.CharField(max_length=50)
    seller_phoneno = models.BigIntegerField()