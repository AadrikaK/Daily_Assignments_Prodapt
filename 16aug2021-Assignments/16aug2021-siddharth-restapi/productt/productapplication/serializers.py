from rest_framework import serializers
from productapplication.models import Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('pname','pcode','pdescp','pprice')