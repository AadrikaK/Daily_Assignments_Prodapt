
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.product_details,name='product_details'),
    path('viewall/', views.product_list,name='product_list'),
]
