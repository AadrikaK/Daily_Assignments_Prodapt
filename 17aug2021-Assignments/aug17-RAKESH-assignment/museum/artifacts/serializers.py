from rest_framework import serializers
from artifacts.models import Artifacts


class ArtifactsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artifacts
        fields=('name','acode','description','location','year')