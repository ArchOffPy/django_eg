from django.db import models
from django.urls import reverse

class Movie(models.Model):
    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True)
    budget = models.IntegerField(default=10000000)
    slug = models.SlugField(default='')

    def get_url(self):
        return reverse('show_one_movies', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating}'