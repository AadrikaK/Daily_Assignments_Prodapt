  
from . import views
from django.urls import path,include

urlpatterns = [
    path('addseller/',views.add_Seller,name='addingSeller'),
    path('viewseller/',views.view_Seller,name='viewingSeller'),
]
