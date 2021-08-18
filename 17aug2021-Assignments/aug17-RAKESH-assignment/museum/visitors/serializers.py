from rest_framework import serializers
from visitors.models import Visitors


class VisitorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Visitors
        fields=('name','ticketno','age','address','phno')