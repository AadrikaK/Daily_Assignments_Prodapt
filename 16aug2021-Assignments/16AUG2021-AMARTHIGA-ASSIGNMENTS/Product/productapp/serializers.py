from django.db.models import fields
from rest_framework import serializers
from productapp.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('ProductName','ProductID', 'Description', 'ProductPrice')