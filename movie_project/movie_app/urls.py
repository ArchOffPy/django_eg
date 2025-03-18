from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies, name='show_all_movies'),
    path('movie/<int:movie_id>', views.show_one_movies, name='show_one_movies'),
]
