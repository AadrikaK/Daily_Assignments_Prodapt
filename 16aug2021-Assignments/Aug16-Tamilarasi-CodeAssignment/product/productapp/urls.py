from django.urls import path, include
from . import views

urlpatterns = [
    path('add/',views.myProductPage,name='myProductPage'),
    path('viewall/',views.myProductList,name='myProductList'),
]