from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.Myaddpage,name='Myaddpage'),
    path('view/',views.seller_list,name='seller_list'),
]
