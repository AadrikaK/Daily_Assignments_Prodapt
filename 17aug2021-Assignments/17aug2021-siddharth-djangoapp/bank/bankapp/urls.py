from . import views
from django.urls import path,include

urlpatterns = [
    path('addstaff/',views.add_Staff,name='add_Staff'),
    path('showstaff/',views.show_Staff,name='show_Staff'),
    path('viewastaff/<id>',views.view_a_Staff,name='view_a_Staff'),
]