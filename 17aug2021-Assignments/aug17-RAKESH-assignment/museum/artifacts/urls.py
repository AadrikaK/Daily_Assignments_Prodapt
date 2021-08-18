from django.urls import path,include
from . import views
urlpatterns=[
    path('addpage/',views.artifactsPage,name='artifactsPage'),
    path('viewall/',views.artifacts_list,name='artifacts_list'),
    path('viewartifacts/<fetchid>',views.artifacts_details,name='artifacts_details'),

]