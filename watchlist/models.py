from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

UserModel = get_user_model()

class Watchlist(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'movie'],
                name='unique_watchlist',
            )
        ]
    def __str__(self):
        return f'{self.user} {self.movie}'