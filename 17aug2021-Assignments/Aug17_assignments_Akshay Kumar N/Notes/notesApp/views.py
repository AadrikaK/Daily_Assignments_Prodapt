from django.http.response import JsonResponse
from notesApp.serializers import NotesSerializers
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from notesApp.serializers import NotesSerializers
from notesApp.models import Notes
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Method to retrieve the data from the database(Retrieve operation)
@csrf_exempt
def notes_list(request):
    if (request.method == "GET"):
        notes = Notes.objects.all()
        notes_serializers = NotesSerializers(notes, many= True)
        return JsonResponse(notes_serializers.data, safe =False)


@csrf_exempt
def  notes_data(request,notesid):
    try:
        notes = Notes.objects.get(notesid = notesid)
        if(request.method == "GET"):
            notes_serializer = NotesSerializers(notes)
            return JsonResponse(notes_serializer.data, safe = False, status=status.HTTP_200_OK)    

        if (request.method == "DELETE"):
            notes.delete()
            return HttpResponse("Deleted", status=status.HTTP_204_NO_CONTENT)

        if (request.method == "PUT"):
            mydict = JSONParser().parse(request)

            notes_serialize = NotesSerializers(notes,data = mydict)
            if (notes_serialize.is_valid()):
                notes_serialize.save()    
                return JsonResponse(notes_serialize.data, status=status.HTTP_200_OK)


    except Notes.DoesNotExist:
        return HttpResponse("Invalid notes ID",status=status.HTTP_404_NOT_FOUND)

    
        





# Method to save or store the data to the database(Create operation)

@csrf_exempt
def notes_add(request):
    if(request.method == "POST"):
        mydict = JSONParser().parse(request)
        notes_serialize = NotesSerializers(data = mydict)
        if (notes_serialize.is_valid()):
            notes_serialize.save()    #Statement used for saving the data to the database.
            return JsonResponse(notes_serialize.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)



        x = json.dumps(mydict)
        return HttpResponse(x)

    else:
        return HttpResponse("GET Method not allowed",status=status.HTTP_404_NOT_FOUND)        
