from rest_framework import serializers
from product.models import Products

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('prodcode','prodname','proddesc','prodprice')  #Here the values of fields should be same as keys of dictionary in views.py 
