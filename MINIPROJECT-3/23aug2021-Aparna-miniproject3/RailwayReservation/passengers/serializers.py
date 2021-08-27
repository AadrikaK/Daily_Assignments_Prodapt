from django.db.models import fields
from rest_framework import serializers
from .models import Passenger, Ticket


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields=('firstName','lastName','gender','email','mobileNumber','username','password','confirm_password')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=('username','email','from_station','to_station','DOJ')

    






