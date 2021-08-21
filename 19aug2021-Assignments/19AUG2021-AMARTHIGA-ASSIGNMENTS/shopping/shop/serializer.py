from rest_framework import serializers
from shop.models import shops
from  django.db.models import fields

class shopSerializer(serializers.ModelSerializer):
    class Meta:
        model = shops
        fields = ('shopname', 'shopadd', 'website', 'phone', 'username', 'password', 'confirmpass')

        