from django.urls import path,include
from . import views
urlpatterns = [
    path('add/',views.Myaddpage,name='Myaddpage'),
    path('view/',views.product_list,name='product_list'),
]
