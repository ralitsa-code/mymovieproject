from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movie

UserModel = get_user_model()

class Review(models.Model):
    review = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        choices=[(1, '1 Star'),
                 (2, '2 Stars'),
                 (3, '3 Stars'),
                 (4, '4 Stars'),
                 (5, '5 Stars'),
    ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['movie', 'user'],
                name='unique_movie_user_review',
            )
        ]
    def __str__(self):
        return f'{self.movie} - {self.user}'


