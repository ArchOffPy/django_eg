from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F


def show_all_movies(request):
    movies = Movie.objects.order_by(F("year").asc(nulls_last=True), 'rating')

    for movie in movies:
        movie.save()

    data = {
        'movies': movies
    }
    return render(request, 'movie_app/all_movies_sorted.html', context=data)


def show_one_movies(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    data = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movies.html', context=data)