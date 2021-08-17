
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from productsapp.models import productsdata

class product_Serializer(serializers.ModelSerializer):
    class Meta:
        model= productsdata
        fields = ('product_name','product_code','product_description','product_price')