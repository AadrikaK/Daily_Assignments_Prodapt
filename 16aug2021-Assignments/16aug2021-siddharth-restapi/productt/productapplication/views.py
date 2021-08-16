from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from productapplication.serializers import ProductSerializers
from productapplication.models import Product
# Create your views here.
@csrf_exempt
def AddProduct(request):
    if(request.method=="POST"):
        pname=request.POST.get("pname")
        pcode=request.POST.get("pcode")
        pdescp=request.POST.get("pdescp")
        pprice=request.POST.get("pprice")
        mydict={"pname":pname,"pcode":pcode,"pdescp":pdescp,"pprice":pprice}
        product_serialize=ProductSerializers(data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            #return HttpResponse("success")
            return response.JsonResponse(product_serialize.data)
            
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method got runned")

@csrf_exempt
def ViewProduct(request):
    if(request.method=='GET'):
        product1=Product.objects.all()
        product_serialize=ProductSerializers(product1,many=True)
        return response.JsonResponse(product_serialize.data,safe=False)
