from django.db import models

# Create your models here.

class Passenger(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    mobileNumber = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)

class Ticket(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField()
    from_station = models.CharField(max_length=40)
    to_station = models.CharField(max_length=40)
    DOJ= models.DateField()
    

    def __str__(self):
        return "%s %s" % (self.ticket_no, self.name)
