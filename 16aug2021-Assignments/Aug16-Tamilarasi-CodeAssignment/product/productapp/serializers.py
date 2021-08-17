from rest_framework import serializers
from productapp.models import Productapp

class ProductappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productapp
        fields=('pro_code','pro_name','pro_description','pro_price')
        