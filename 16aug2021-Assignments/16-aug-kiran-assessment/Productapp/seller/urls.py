from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.selleradd,name='selleradd'),
    path('viewall/',views.seller_list,name='seller_list'),
]