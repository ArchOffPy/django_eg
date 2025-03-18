from django.shortcuts import render, get_object_or_404
from .models import Movie


def show_all_movies(request):
    movies = Movie.objects.all()
    data = {
        'movies': movies
    }
    return render(request, 'movie_app/all_movies.html', context=data)


def show_one_movies(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    data = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movies.html', context=data)