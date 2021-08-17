from django.urls import path,include
from . import views
urlpatterns=[
    path('add/',views.productAddPage,name='productAddPage'),
    path('viewall/',views.product_list,name='product_list'),
    
    
]