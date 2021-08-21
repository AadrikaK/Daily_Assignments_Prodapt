from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from starconstellation.serializers import StarSerializer
from starconstellation.models import Star
from rest_framework.parsers import JSONParser
from rest_framework import status


def constellation(request):
    #return HttpResponse(" <input    /> <button>Login</button> <h1> Hi, Welcome </h1> ")
    return render(request,'index.html')

@csrf_exempt
def connectstars(request):
    if(request.method == 'POST'):
        star = JSONParser().parse(request)
        star_serial= StarSerializer(data=star)
        if(star_serial.is_valid()):
            star_serial.save()
            return JsonResponse(star_serial.data, status = status.HTTP_200_OK)

        else:
            return HttpResponse('Serialization Erros', status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse('Hello, welcome to Star Constellation Application')

@csrf_exempt
def viewstars(request):
    if(request.method =='GET'):
        stars = Star.objects.all()
        stars_serializer = StarSerializer(stars, many=True)
        return JsonResponse(stars_serializer.data, safe=False, status = status.HTTP_200_OK)

    else:
        return HttpResponse('Serialization Erros', status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def stars_UD(request, id):
    try:
        stars = Star.objects.get(id=id)
        if(request.method =='GET'):
            star_serializer = StarSerializer(stars)
            return JsonResponse(star_serializer.data, safe= False, status= status.HTTP_200_OK)

        if(request.method == 'DELETE'):
            stars.delete()
            return HttpResponse("The star details have been deleted", status = status.HTTP_204_NO_CONTENT)

        if(request.method =='PUT'):
            star =JSONParser().parse(request)
            star_serialize = StarSerializer(star, data=star)
            if(star_serialize.is_valid()):
                star_serialize.save()
                return JsonResponse(star_serialize.data, status= status.HTTP_200_OK)


    except Star.DoesNotExist:
        return HttpResponse("Invalid", Status = status.HTTP_404_NOT_FOUND)




