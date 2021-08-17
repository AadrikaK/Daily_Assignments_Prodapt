from . import views
from django.urls import path,include

urlpatterns = [
    path('addproduct/',views.add_Product,name='addingProduct'),
    path('viewproduct/',views.view_Product,name='viewingProduct'),
]
