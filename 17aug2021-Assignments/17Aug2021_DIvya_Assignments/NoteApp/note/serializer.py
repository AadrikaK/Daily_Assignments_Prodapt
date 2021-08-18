from django.db.models import fields
from rest_framework import serializers
from note.models import Notes

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields = ('title','desc')