from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.productadd,name='productadd'),
    path('viewall/',views.product_list,name='product_list'),
]