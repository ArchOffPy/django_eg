from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies, name='show_all_movies'),
    path('movie/<slug:slug_movie>', views.show_one_movies, name='show_one_movies'),
    path('directors', views.show_all_directors, name='show_all_directors'),
    path('directors/<int:id_director>', views.show_one_director, name='show_one_director'),
]
