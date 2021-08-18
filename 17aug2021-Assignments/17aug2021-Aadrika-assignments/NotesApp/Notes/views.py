from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from Notes.serializer import NoteSerializer
from Notes.models import Note
from rest_framework.parsers import JSONParser
from rest_framework import status





##################### adding notes to db ######################
@csrf_exempt
def addNote(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        noteserialize=NoteSerializer(data=mydata)
        if (noteserialize.is_valid()):
            noteserialize.save() 
            return response.JsonResponse(noteserialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization process of notes")

########### viewing all the content #############################
@csrf_exempt
def viewNote(request):
    if (request.method=='GET'):
        notes=Note.objects.all()
        noteserializer=NoteSerializer(notes,many=True)
        return response.JsonResponse(noteserializer.data, safe=False,status=status.HTTP_200_OK)

################# viewing ,deleting and updating single details ######################################
@csrf_exempt
def viewnotedetails(request,id):
    try:
        notes=Note.objects.get(id=id)
        if (request.method=='GET'):
            noteserializer=NoteSerializer(notes) 
            return response.JsonResponse(noteserializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            notes.delete()
            return HttpResponse("deleted notes")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            noteserial=NoteSerializer(notes,data=mydata)
            if (noteserial.is_valid()):
                noteserial.save()
                return response.JsonResponse(noteserial.data,status=status.HTTP_200_OK)
    except Note.DoesNotExist:
        return HttpResponse("invalid ID for notes")


    