from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

UserModel = get_user_model()

class Favorite(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['movie', 'user'],
                name='unique_favorite',
            )
        ]

    def __str__(self):
        return self.movie.title
