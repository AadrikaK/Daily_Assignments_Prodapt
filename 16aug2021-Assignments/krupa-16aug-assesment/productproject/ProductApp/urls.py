from django.urls import path,include
from.import views

urlpatterns=[
    path('', views.product, name='product'),
    path('add/', views.product_list, name='product_list'),
    
]