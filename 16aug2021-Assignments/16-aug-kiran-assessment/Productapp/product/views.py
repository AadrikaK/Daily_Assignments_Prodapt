from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializers import ProductSerializer
from product.models import Product
# Create your views here.
@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=ProductSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)
@csrf_exempt
def productadd(request):
    if(request.method=='POST'):
        pname=request.POST.get("pname")
        pcode=request.POST.get("pcode")
        description=request.POST.get("description")
        price=request.POST.get("price")
        dict={"pname":pname,"pcode":pcode,"description":description,"price":price}
        product_serialize=ProductSerializer(data=dict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method")