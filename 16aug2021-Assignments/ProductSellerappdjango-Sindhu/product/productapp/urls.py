from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.productapp_create,name='productapp_create'),
    path('viewall/',views.productapp_list,name='productapp_list'),
]