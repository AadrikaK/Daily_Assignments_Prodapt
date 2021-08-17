from . import views
from django.urls import path,include

urlpatterns = [
    path('addproduct/',views.AddProduct,name='AddProduct'),
    path('viewproduct/',views.ViewProduct,name='ViewProduct'),
]