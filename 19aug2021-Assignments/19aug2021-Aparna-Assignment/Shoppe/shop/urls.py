from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.add_shop,name="add_shop"),
    path('addshop/',views.shopPage,name="shopPage"),
    path('viewall/',views.shop_list,name='shop_list'),
    path('viewshop/<id>',views.shop_details,name='shop_details'),


    
]