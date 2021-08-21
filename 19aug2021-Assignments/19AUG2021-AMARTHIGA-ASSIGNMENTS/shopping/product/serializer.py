from rest_framework import serializers
from  django.db.models import fields
from product.models import products

class proSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = ('proname', 'prodetail', 'seller', 'manufacturer', 'manudate', 'expirydate', 'price' )
