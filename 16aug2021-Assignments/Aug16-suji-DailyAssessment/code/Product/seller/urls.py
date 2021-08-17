from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.sellerAddPage,name='sellerAddPage'),
    path('viewall/',views.seller_list,name='seller_list'),
    
    
]