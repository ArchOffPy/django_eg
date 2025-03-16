from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()

    def __str__(self):
        return f"Книга: {self.title}\nРейтин: {self.rating}"