from django.urls import path,include
from.import views

urlpatterns=[
    path('pro/', views.product, name='product'),
    path('view/',views.product_list,name='product_list'),
]