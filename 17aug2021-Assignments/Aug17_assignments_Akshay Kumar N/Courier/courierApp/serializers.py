from courierApp.models import Courier
from rest_framework import serializers
from courierApp.models import Courier

class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ('cid','cname','cdeladdress','cpincode')