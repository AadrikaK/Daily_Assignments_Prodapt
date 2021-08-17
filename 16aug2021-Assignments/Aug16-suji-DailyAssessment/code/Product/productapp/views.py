from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.serializers import ProductSerializer
from productapp.models import Product1

# Create your views here.

@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product1.objects.all()
        product_serialize=ProductSerializer(products,many=True)
        return JsonResponse(product_serialize.data,safe=False)



@csrf_exempt
def productAddPage(request):
    if request.method=="POST":
        getName=request.POST.get("pname")
        getDescription=request.POST.get("description")
        getCode=request.POST.get("code")
        getPrice=request.POST.get("price")
        mydata={"pname":getName,"description":getDescription,"code":getCode,"price":getPrice};
        #result=json.dumps(mydict)
        #return HttpResponse(result)
        product_serialize=ProductSerializer(data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("Error in serialization")

    else:     
        return HttpResponse("No get method allowed")   
