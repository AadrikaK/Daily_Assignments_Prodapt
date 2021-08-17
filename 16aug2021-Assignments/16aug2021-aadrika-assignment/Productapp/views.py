from Productapp.serialize import ProductSerializers
from Productapp.models import Product
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def view_Product(request):
    if(request.method=='GET'):
        product1=Product.objects.all()
        product_serialize=ProductSerializers(product1,many=True)
        return response.JsonResponse(product_serialize.data,safe=False)


@csrf_exempt
def add_Product(request):
    if(request.method=="POST"):
        getpname=request.POST.get("pname")
        getpcode=request.POST.get("pcode")
        getpdescp=request.POST.get("pdescp")
        getpprice=request.POST.get("pprice")
        mydict={"pname":getpname,"pcode":getpcode,"pdescp":getpdescp,"pprice":getpprice}
        product_serialize=ProductSerializers(data=mydict)
        if(product_serialize.is_valid()):
            product_serialize.save()
            
            return response.JsonResponse(product_serialize.data)
            
        else:
            return HttpResponse("error in serialization of process")
    else:
        return HttpResponse("GET method is not  runned")

