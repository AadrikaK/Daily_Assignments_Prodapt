from rest_framework import serializers
from productapp.models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('pcode','pname','des','price')