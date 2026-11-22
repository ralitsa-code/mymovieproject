from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.generic import ListView, View, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from movies.models import Movie
from .models import Favorite


class FavoriteListView(LoginRequiredMixin, ListView):
    model = Favorite
    template_name = 'favorites/favorite_list.html'

    def get_queryset(self):
        user = self.request.user
        return Favorite.objects.filter(user=user)


@method_decorator(require_POST, name='dispatch')
class FavoriteAddView(LoginRequiredMixin, View):

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)

        Favorite.objects.get_or_create(user=request.user, movie=movie)

        return redirect('movie-detail', pk=movie.pk)

class FavoriteDeleteView(LoginRequiredMixin, DeleteView):
    model = Favorite
    success_url = reverse_lazy('favorites')

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)