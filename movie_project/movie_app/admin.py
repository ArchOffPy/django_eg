from django.contrib import admin
from .models import Movie

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'rating_status']
    list_editable = ['rating', 'year']
    ordering = ['rating', 'name']
    list_per_page = 3

    @admin.display(ordering='rating', description='Rating')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Плохой фильм'
        if mov.rating < 75:
            return 'Средний фильм'
        if mov.rating <= 85:
            return 'Хороший фильм'

        return 'Отличный фильм'



