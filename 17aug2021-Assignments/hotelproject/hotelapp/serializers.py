from rest_framework import serializers
from hotelapp.models import hotel

class hotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=hotel
        fields=('name','adress','phno','rno')