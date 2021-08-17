from django.db import models

# Create your models here.
class Sellerapp(models.Model):
    sell_id=models.IntegerField()
    sell_name=models.CharField(max_length=50)
    sell_address=models.CharField(max_length=50)
    sell_mblno=models.BigIntegerField()
