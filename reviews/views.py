from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
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

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_update.html'
    pk_url_kwarg = 'review_id'

    def get_queryset(self):
        user_reviews = super().get_queryset().filter(user=self.request.user)
        return user_reviews

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['movie'] = self.object.movie
        return kwargs

    def get_success_url(self):
        return reverse_lazy(
            'movie-detail',
            kwargs={'pk': self.object.movie.pk}
        )

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews/review_delete.html'
    pk_url_kwarg = 'review_id'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.object.movie.pk})




