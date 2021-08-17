
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.seller_details,name='seller_details'),
    path('viewall/', views.seller_list,name='seller_list'),
]
