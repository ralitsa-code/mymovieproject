from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from movies.models import Movie
from reviews.forms import ReviewForm
from reviews.models import Review


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_create.html'

    def get_success_url(self):
        movie_pk = self.kwargs.get('pk')
        return reverse_lazy('movie-detail', kwargs={'pk': movie_pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        kwargs['movie'] = movie
        return kwargs
