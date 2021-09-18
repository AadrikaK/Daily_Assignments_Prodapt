from django.db import models
from datetime import datetime
class Admin(models.Model):
    adminname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class Prepaid(models.Model):
    prename=models.CharField(max_length=50)
    preamount=models.CharField(max_length=50)
    prevalidity=models.CharField(max_length=50)
    prebenefits=models.CharField(max_length=1000)
    preofferdiscount=models.CharField(max_length=500)

class Postpaid(models.Model):
    postname=models.CharField(max_length=50)
    postamount=models.CharField(max_length=50)
    postvalidity=models.CharField(max_length=50)
    postbenefits=models.CharField(max_length=1000)
    postofferdiscount=models.CharField(max_length=500)
    
class Dongle(models.Model):
    planname=models.CharField(max_length=50)
    dongleamount=models.CharField(max_length=50)
    donglevalidity=models.CharField(max_length=100,default="")
    dongleofferdiscount=models.CharField(max_length=500)
    typeofservices=models.CharField(max_length=50,default="")
    donglebenefits=models.CharField(max_length=500,default="")

    
class Customer(models.Model):
    
    cname =models.CharField(max_length=50)
    address =models.CharField(max_length=50)
    mobno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    aadharno=models.BigIntegerField()
    password=models.CharField(max_length=20)
    profilep=models.ImageField(default="")
    adhaarp=models.ImageField(default="")


class Queries(models.Model):
    mobno=models.CharField(max_length=50)
    queryname=models.CharField(max_length=50)
    querydes=models.CharField(max_length=100)
    querysolution=models.CharField(max_length=50,default="")

class Prepaidinvoice(models.Model):
    mobno=models.CharField(max_length=25)
    typeservices=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)
    pamount=models.CharField(max_length=50)
    paymentmethod=models.CharField(max_length=50)
    curdate=models.CharField(max_length=50,default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

# class Serviceuses(models.Model):

#     servicecategory=models.CharField(max_length=50)
class Usage(models.Model):
    mobilen=models.CharField(max_length=50,default=True)
    curplan=models.CharField(max_length=50,default=True)
    extracall=models.CharField(max_length=50,default=True)
    extrasms=models.CharField(max_length=50,default=True)
    extradata=models.CharField(max_length=50,default=True)
   
    
class Bill(models.Model):
    mobile=models.CharField(max_length=50)
    curplancharge=models.CharField(max_length=50)
    extracallcharge=models.CharField(max_length=50)
    extrasmscharge=models.CharField(max_length=50)
    extradatacharges=models.CharField(max_length=50)
    totalamount=models.CharField(max_length=50,default=True)
    currdate=models.CharField(max_length=50,default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


    




