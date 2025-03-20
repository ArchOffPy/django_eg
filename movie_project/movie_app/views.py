from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Max, Min, Count, Avg, Value


def show_all_movies(request):
    # movies = Movie.objects.order_by(F("year").asc(nulls_last=True), 'rating')
    movies = Movie.objects.annotate(
        new_budget=F('budget') + 123,
        new_rating=F('rating') * 2,
        rating_and_year=F('rating') + F('year'),
    )

    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))

    data = {
        'movies': movies,
        'agg': agg,
        'total': movies.count(),
    }
    return render(request, 'movie_app/all_movies_sorted.html', context=data)


def show_one_movies(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    data = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movies.html', context=data)