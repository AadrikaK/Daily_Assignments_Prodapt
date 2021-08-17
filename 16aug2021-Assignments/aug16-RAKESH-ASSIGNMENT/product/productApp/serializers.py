from rest_framework import serializers
from productApp.models import Product


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=('pname','pcode','description','price')