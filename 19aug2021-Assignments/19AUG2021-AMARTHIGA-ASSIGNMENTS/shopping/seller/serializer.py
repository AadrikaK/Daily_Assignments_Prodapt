from rest_framework import serializers
from  django.db.models import fields
from seller.models import sellers

class selSerializer(serializers.ModelSerializer):
    class Meta:
        model = sellers
        fields = ('sellername','address','email', 'phone', 'dateofbirth', 'age', 'aadhar')