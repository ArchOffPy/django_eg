from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"Книга: {self.title}\nРейтин: {self.rating}"