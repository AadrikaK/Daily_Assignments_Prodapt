from django.db.models import fields
from rest_framework import serializers
from Productapp.models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('pname','pcode','pdescp','pprice')
