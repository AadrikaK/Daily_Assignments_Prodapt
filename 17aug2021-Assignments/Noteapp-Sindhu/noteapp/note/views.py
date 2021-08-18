from django.shortcuts import render
from note.models import Note
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from note.serializers import NoteSerializer
from note.models import Note
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.
@csrf_exempt
def note_details(request,ntitle):
    try:
        note=Note.objects.get(ntitle=ntitle)
        if(request.method=="GET"):
            note_serializer=NoteSerializer(notesapp)
            return JsonResponse(note_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            note.delete()
            return HttpResponse("Delete",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            note_serialize=NoteSerializer(note,data=mydata)
            if(note_serialize.is_valid()):
                note_serialize.save()
                return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(note_serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    except Note.DoesNotExist:
        return HttpResponse("Invalid Voterid",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def note_list(request):
    if(request.method=="GET"):
        note=Note.objects.all()
        note_serializer=NoteSerializer(note,many=True)
        return JsonResponse(note_serializer.data,safe=False)
@csrf_exempt
def note_create(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        note_serialize=NoteSerializer(data=mydata)
        if(note_serialize.is_valid()):
            note_serialize.save()
            return JsonResponse(note_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)
