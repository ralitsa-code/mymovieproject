from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import ListView, View, DeleteView
from django.urls import reverse_lazy

from movies.models import Movie
from watchlist.models import Watchlist

class WatchlistListView(LoginRequiredMixin, ListView):
    model = Watchlist
    template_name = 'watchlist/watchlist.html'

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)

@method_decorator(require_POST, name='dispatch')
class WatchlistAddView(LoginRequiredMixin, View):

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)

        Watchlist.objects.get_or_create(
            user=request.user,
            movie=movie,
        )

        return redirect('movie-detail', pk=movie.pk)

class WatchlistDeleteView(LoginRequiredMixin, DeleteView):
    model = Watchlist
    success_url = reverse_lazy('watchlist')

    def get_queryset(self):
        return Watchlist.objects.filter(user=self.request.user)
