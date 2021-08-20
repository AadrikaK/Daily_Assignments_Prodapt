from django.urls import path,include
from.import views

urlpatterns=[
    path('', views.seller, name='seller'),
    path('add/', views.seller_list, name='seller_list'),
    
]