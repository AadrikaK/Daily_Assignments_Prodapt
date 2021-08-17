from rest_framework import serializers
from bankapp.models import Banking

class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model=Banking
        fields=('code','name','desig','sal')