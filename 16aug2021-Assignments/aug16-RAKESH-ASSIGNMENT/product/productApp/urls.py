from django.urls import path,include
from . import views
urlpatterns = [
  
    path('addpage/',views.productPage,name='productPage'),
    path('viewall/',views.product_list,name='product_list'),

] 