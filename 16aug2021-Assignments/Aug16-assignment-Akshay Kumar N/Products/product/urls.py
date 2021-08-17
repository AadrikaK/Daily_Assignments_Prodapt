from  django.urls import path, include
from . import views

urlpatterns = [

    path('add/', views.products_add, name = 'products_add'),
    path('viewall/',views.products_list, name ='products_list'),
    
]