from django.urls import path,include
from.import views

urlpatterns=[
    path('sell/', views.seller, name='seller'),
    path('view/',views.seller_list,name='seller_list'),
]