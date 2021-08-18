from django.db import models
from django.db.models import fields
from rest_framework import serializers
from notes.models import Notes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields=('title','description')