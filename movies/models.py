from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ApprovalModel(models.Model):

    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    class Meta:
        abstract = True


class Genre(ApprovalModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Actor(ApprovalModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Director(ApprovalModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Movie(ApprovalModel):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='movies')
    genre = models.ManyToManyField(Genre, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    director = models.ManyToManyField(Director, blank=True)
    description = models.TextField()
    year = models.PositiveIntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='movies')

    def clean(self):
        super().clean()
        if self.year and self.year > date.today().year:
            raise ValidationError({'year': 'Year cannot be in the future!'})

    def __str__(self):
        return self.title




