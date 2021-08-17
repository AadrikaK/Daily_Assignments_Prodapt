from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from notes.serializers import NoteSerializers
from notes.models import Note
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def note_add(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        note_serialize=NoteSerializers(data=mydict)
        if(note_serialize.is_valid()):
            note_serialize.save()
            return response.JsonResponse(note_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("error in serialization part of code",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method executed")

@csrf_exempt
def all_notes(request):
    if(request.method=='GET'):
        note1=Note.objects.all()
        note_serialize=NoteSerializers(note1,many=True)
        return response.JsonResponse(note_serialize.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def note_info(request,id):
    try:
        note1=Note.objects.get(id=id)
    except:
        return HttpResponse("Invalid note title",)
    
    if(request.method=='GET'):
        
        note_serialize=NoteSerializers(note1)
        return response.JsonResponse(note_serialize.data,safe=False)
    
    if(request.method=='PUT'):
        mydict=JSONParser().parse(request)
        note_serialize=NoteSerializers(note1,data=mydict)
        if (note_serialize.is_valid()):
            note_serialize.save()
            return response.JsonResponse(note_serialize.data)

    if(request.method=='DELETE'):
        note1.delete()
        return HttpResponse("notes deleted")


