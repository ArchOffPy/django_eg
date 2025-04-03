from django.contrib import admin, messages
from .models import Movie, Director
from django.db.models import QuerySet

# Register your models here.

admin.site.register(Director)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('0-29', 'Низкий'),
            ('30-59', 'Средний'),
            ('60-79', 'Высокий'),
            ('80-100', 'Наилучший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '0-29':
            return queryset.filter(rating__lt=30)
        if self.value() == '30-59':
            return queryset.filter(rating__gte=30).filter(rating__lt=60)
        if self.value() == '60-79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        if self.value() == '80-100':
            return queryset.filter(rating__gte=80)
        return queryset




@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['rating', 'name']
    # exclude = ['slug']
    # readonly_fields = ['budget']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'year', 'currency', 'rating_status', 'director']
    list_editable = ['rating', 'year', 'currency', 'director']
    ordering = ['rating', 'name']
    list_per_page = 10
    actions = ['set_rubel', 'set_dollar']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', RatingFilter, 'currency', ]

    @admin.display(ordering='rating', description='Rating')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Плохой фильм'
        if mov.rating < 75:
            return 'Средний фильм'
        if mov.rating <= 85:
            return 'Хороший фильм'

        return 'Отличный фильм'

    @admin.action(description="Установить валюту Рубль")
    def set_rubel(self, request, qs: QuerySet):
        qs.update(currency=Movie.RUB)

    @admin.action(description="Установить валюту Доллар")
    def set_dollar(self, request, qs: QuerySet):
        count = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f'Было обновлено {count} записей.',
            messages.ERROR
        )


