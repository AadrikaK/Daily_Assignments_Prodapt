from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse

from product.models import products
from product.serializer import proSerializer

# Create your views here.
def regpro(request):
    return render(request, 'addpro.html')

@csrf_exempt
def addpro(request):
    if(request.method =='POST'):
        prodata = JSONParser().parse(request)
        pro_serialize = proSerializer(data=prodata)

        if(pro_serialize.is_valid()):
            pro_serialize.save()
            return JsonResponse(pro_serialize.data, status = status.HTTP_200_OK)

        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome all to product page!")

@csrf_exempt
def viewpro(request):
    if(request.method == 'GET'):
        pro=products.objects.all()
        pro_serializer = proSerializer(pro, many=True)
        return JsonResponse(pro_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view shop details!")

@csrf_exempt
def details(request, id):
    try:
        pro = products.objects.get(id = id)
        if (request.method == 'GET'):
            pro_serialize = proSerializer(pro)
            return JsonResponse(pro_serialize.data, safe = False, status=status.HTTP_200_OK)
        if (request.method == "DELETE"):
                    pro.delete()
                    return HttpResponse("Content Deleted", status=status.HTTP_204_NO_CONTENT)
        if(request.method =='PUT'):
             prodata = JSONParser().parse(request)
             pro_serialize = proSerializer(pro, data=prodata)
             if(pro_serialize.is_valid()):
                 pro_serialize.save()
                 return JsonResponse(pro_serialize.data, status=status.HTTP_200_OK)

        
    except products.DoesNotExist:
        return HttpResponse("Invalid Employee Id", status=status.HTTP_400_BAD_REQUEST)

