from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from product.serializer import ProductSerializer
from product.models import Product

# Create your views here.
@csrf_exempt
def product_list(request):
    if(request.method == "GET"):
        products = Product.objects.all()
        product_serialize = ProductSerializer(products,many = True)
        return JsonResponse(product_serialize.data,safe= False)


@csrf_exempt
def addpage(request):
    if (request.method == "POST"):
        getName = request.POST.get("name")
        getcode = request.POST.get("pro_code")
        getdesc = request.POST.get("pro_desc")
        geteprice = request.POST.get("pro_price")
        mydata = {"name":getName,"pro_code":getcode,"pro_desc":getdesc,"pro_price":geteprice};
        product_serialize=ProductSerializer(data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
            
        else:
            return HttpResponse("Error in serialization")

         
    else:
        return HttpResponse("thank you")
