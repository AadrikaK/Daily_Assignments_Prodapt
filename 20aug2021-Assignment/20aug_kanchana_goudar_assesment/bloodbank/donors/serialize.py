from rest_framework import serializers
from donors.models import Donor

class DonorSerialize(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('Blood_group','Name','Adress','Pincode','Mobileno','Last_donated_date')