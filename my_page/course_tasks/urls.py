from django.urls import path
from . import views as views

urlpatterns = [
    path('actors', views.actors, name='actors'),
    path('records', views.get_guinness_world_records, name='events'),
]



