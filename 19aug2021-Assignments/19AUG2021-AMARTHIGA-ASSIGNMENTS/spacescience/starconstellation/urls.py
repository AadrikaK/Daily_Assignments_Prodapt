
from django.urls import  path, include, re_path
from starconstellation import views

urlpatterns = [
    path('', views.constellation, name='constellation'),
    path('connect/', views.connectstars, name='connectstars'),
    path('viewstars/', views.viewstars, name='viewstars'),
    path('view/<id>', views.stars_UD, name='stars_UD'),

]