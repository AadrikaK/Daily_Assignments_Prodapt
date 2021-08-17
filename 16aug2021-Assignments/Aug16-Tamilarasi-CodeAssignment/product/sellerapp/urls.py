from django.urls import path, include
from . import views

urlpatterns = [
    path('add/',views.mySellerPage,name='mySellerPage'),
    path('viewall/',views.mySellerList,name='mySellerList'),
]