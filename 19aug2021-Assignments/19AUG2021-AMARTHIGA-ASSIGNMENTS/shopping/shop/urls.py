from django.urls import path, include
from shop import views

urlpatterns =[
    path('register/', views.register, name= 'register'),
    path('addshop/', views.addshop, name= 'addshop'),
    path('viewshop/', views.viewshop, name= 'viewshop'),
    path('details/<id>', views.shopdetails, name= 'shopdetails'),
]
