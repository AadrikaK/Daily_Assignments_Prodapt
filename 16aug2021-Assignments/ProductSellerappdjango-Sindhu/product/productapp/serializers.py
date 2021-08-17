from rest_framework import serializers
from productapp.models import Productapp

class ProductappSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productapp
        fields=('pcode','pname','pdescription','pprice')
