from django.urls import path,include
from .import views

urlpatterns = [
    path('add/',views.product_create, name='product_create'),
    path('viewall/',views.product_list,name='product_list'),
]