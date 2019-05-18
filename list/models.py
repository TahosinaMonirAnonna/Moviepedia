from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    director = models.CharField(max_length=40)

    def __str__(self):
        return self.title

# Create your models here.
