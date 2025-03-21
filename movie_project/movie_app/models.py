from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    CURRENCY_CHOICES = [
        ('E', 'Euro'),
        ('U', 'United States Dollar'),
        ('R', 'Russian Rub'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField()
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=10000000)
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, default='R')
    slug = models.SlugField(default='', null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('show_one_movies', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}'
