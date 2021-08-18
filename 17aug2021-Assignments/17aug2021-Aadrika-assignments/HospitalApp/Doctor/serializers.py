from rest_framework import serializers
from Doctor.models import Doctors

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctors
        fields=('dname','dadd','dmob','did')