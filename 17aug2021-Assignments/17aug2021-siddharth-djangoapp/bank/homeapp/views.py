from django.shortcuts import render
from django.http import HttpResponse

def viewHomepage(request):
    return HttpResponse("Welcome to FDFC Bank")
def contactUs(request):
    return HttpResponse("For any queries contact to our customer support- 9425171349")

