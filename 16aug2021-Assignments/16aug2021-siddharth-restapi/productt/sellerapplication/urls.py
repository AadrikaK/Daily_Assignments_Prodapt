from . import views
from django.urls import path,include

urlpatterns = [
    path('addseller/',views.AddSeller,name='AddSeller'),
    path('viewseller/',views.ViewSeller,name='ViewSeller'),
]