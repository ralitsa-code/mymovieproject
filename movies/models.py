from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Actor(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Director(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='movies')
    genre = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    director = models.ManyToManyField(Director, blank=True)
    description = models.TextField()
    year = models.PositiveIntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='movies')

    def __str__(self):
        return self.title





