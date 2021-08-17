from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.addpage,name='addpage'),
    path('viewall/',views.product_list,name='product_list'),
]