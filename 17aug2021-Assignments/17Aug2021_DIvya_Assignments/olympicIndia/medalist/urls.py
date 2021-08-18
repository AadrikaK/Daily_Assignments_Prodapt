from django.urls import path,include
from . import views
urlpatterns = [
    path('medalistadd/',views.addpage,name='addpage'),
    path('viewall/',views.medal_list,name='medal_list'),
    path('view/<id>',views.medalpage,name='medalpage')
]