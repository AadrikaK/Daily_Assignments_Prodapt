from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productApp.serializers import productSerializer
from productApp.models import Product
# Create your views here.


@csrf_exempt
def product_list(request):
    if(request.method=="GET"):
        products=Product.objects.all()
        product_serializer=productSerializer(products,many=True)
        return JsonResponse(product_serializer.data,safe=False)


@csrf_exempt
def productPage(request):
    if(request.method=="POST"):
        getName=request.POST.get("pname")
        getcode=request.POST.get("pcode")
        getDescription=request.POST.get("description")
        getPrice=request.POST.get("price")
        mydata={"pname":getName,"pcode":getcode,"description":getDescription,"price":getPrice}
        product_serialize=productSerializer(data=mydata)
        if(product_serialize.is_valid()):
            product_serialize.save()
            # return HttpResponse("Success")
            return JsonResponse(product_serialize.data)

        else:
            return HttpResponse("Error in serialization")    
        # result=json.dumps(mydict)
        # return HttpResponse(mydata)
    else:
        return HttpResponse("No GET method Allowed")
