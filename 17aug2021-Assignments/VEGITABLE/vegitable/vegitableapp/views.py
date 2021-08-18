from django.http.response import JsonResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from vegitableapp.serializers import VegitableSerializer
from vegitableapp.models import Vegitableapp1
from rest_framework.parsers import JSONParser
from rest_framework import status


@csrf_exempt
def vegitable_list(request):
    if(request.method == "GET"):
        vegitables = Vegitableapp1.objects.all()
        Vegitable_Serializer= VegitableSerializer(vegitables, many=True)
        return JsonResponse(Vegitable_Serializer.data, safe=False)

@csrf_exempt
def vegitabledetail(request,fetchid):
    try:
        vegitables=Vegitableapp1.objects.get(vegitableid=fetchid)
        if(request.method == "GET"):
            Vegitable_Serializer=VegitableSerializer(vegitables)
            return JsonResponse(Vegitable_Serializer.data, safe=False, status=status.HTTP_200_OK)

        if(request.method=="DELETE"):
            vegitables.delete()
            return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)

        if(request.method == "PUT"):
            mydata=JsonResponse().parse(request)
            Vegitable_Serializer = VegitableSerializer(data=mydata)
            if(Vegitable_Serializer.is_valid()):
                Vegitable_Serializer.save()
                return JsonResponse(Vegitable_Serializer.data,status=status.HTTP_200_OK)

    except Vegitableapp1.DoesNotExist:
        return HttpResponse("Invalid Vegitable id",status=status.HTTP_404_NOT_FOUND)

        

@csrf_exempt
def vegitable(request):
    if(request.method=="POST"):
        mydata = JSONParser().parse(request)
        Vegitable_Serializer = VegitableSerializer(data=mydata)
        if(Vegitable_Serializer.is_valid()):
            Vegitable_Serializer.save()
            return JsonResponse(Vegitable_Serializer.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("No get method",status=status.HTTP_404_NOT_FOUND)


