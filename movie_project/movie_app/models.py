from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_url(self):
        return reverse("show_one_director", args=[self.id])


class Actor(models.Model):
    # константы для поля choice
    MALE = 'M'
    FEMALE = 'F'
    # список для поля choice
    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # в параметре choces указываем список кортежей GENDERS, и значение по умолчанию MALE
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        # если пол мужской, то отображаем "Актер... имя, фамилия"
        if self.gender == self.MALE:
            return f"Актер {self.first_name} {self.last_name}"
        # если женский, то "Актриса... имя, фамилия"
        return f"Актриса {self.first_name} {self.last_name}"

    def get_url(self):
        return reverse("show_one_actors", args=[self.id])


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'United States Dollar'),
        (RUB, 'Russian Rub'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=10000000, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    # связь одни ко многим с моделью Director
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    # связь многие ко многим с моделью Actor
    actors = models.ManyToManyField(Actor, related_name='movies')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('show_one_movies', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
