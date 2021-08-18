from django.urls import path,include
from . import views
urlpatterns=[
    path('addpage/',views.visitorsPage,name='visitorsPage'),
    path('viewall/',views.visitors_list,name='visitors_list'),
    path('viewvisitors/<fetchid>',views.visitors_details,name='visitors_details'),

]