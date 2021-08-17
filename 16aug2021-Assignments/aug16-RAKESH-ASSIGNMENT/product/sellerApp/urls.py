from django.urls import path,include
from . import views
urlpatterns = [
  
    path('addpage/',views.sellerPage,name='sellerPage'),
    path('viewall/',views.seller_list,name='seller_list'),

] 