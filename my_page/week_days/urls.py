from django.urls import path
from . import views as views

urlpatterns = [
    path('monday', views.monday),
    path('tuesday', views.tuesday),
]