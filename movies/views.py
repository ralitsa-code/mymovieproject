from django.db.models import Model
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from movies.models import Movie, Genre, Actor, Director
from movies.forms import MovieCreateForm, MovieDeleteForm, GenreCreateForm, ActorCreateForm, DirectorCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from movies.serializers import MovieSerializer
from rest_framework.permissions import AllowAny


class UserSubmissionMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'movies/home.html'

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        approved_movies = super( ).get_queryset().filter(status=Movie.APPROVED)
        return approved_movies


class MyMoviesView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'movies/my_movies.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(user=self.request.user)

class MovieCreateView(LoginRequiredMixin, UserSubmissionMixin, CreateView):
    model = Movie
    form_class = MovieCreateForm
    template_name = 'movies/movie_create.html'

    def get_success_url(self):
        return f"{reverse('submission_success')}?type=movie"


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

    def get_queryset(self):
        approved_movies = super( ).get_queryset().filter(status=Movie.APPROVED)
        return approved_movies


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieCreateForm
    template_name = 'movies/movie_update.html'


    def get_queryset(self):
        user_movies = super( ).get_queryset().filter(user=self.request.user)
        return user_movies

    def get_success_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.object.pk})


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    form_class = MovieDeleteForm
    template_name = 'movies/movie_delete.html'
    success_url = reverse_lazy('my-movies')


    def get_queryset(self):
        user_movies = super( ).get_queryset().filter(user=self.request.user)
        return user_movies

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs




class GenreCreateView(LoginRequiredMixin, UserSubmissionMixin, CreateView):
    model = Genre
    form_class = GenreCreateForm
    template_name = 'movies/genre_create.html'

    def get_success_url(self):
        return f"{reverse('submission_success')}?type=genre"

class GenreListView(LoginRequiredMixin, ListView):
    model = Genre
    template_name = 'movies/genre_list.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return Genre.objects.filter(user=self.request.user)

class GenreUpdateView(LoginRequiredMixin, UpdateView):
    model = Genre
    form_class = GenreCreateForm
    template_name = 'movies/genre_update.html'
    success_url = reverse_lazy('genre-list')

    def get_queryset(self):
        return Genre.objects.filter(user=self.request.user)

class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = 'movies/genre_delete.html'
    success_url = reverse_lazy('genre-list')

    def get_queryset(self):
        return Genre.objects.filter(user=self.request.user)


class DirectorCreateView(LoginRequiredMixin, UserSubmissionMixin, CreateView):
    model = Director
    form_class = DirectorCreateForm
    template_name = 'movies/director_create.html'

    def get_success_url(self):
        return f"{reverse('submission_success')}?type=director"

class ActorCreateView(LoginRequiredMixin, UserSubmissionMixin, CreateView):
    model = Actor
    form_class = ActorCreateForm
    template_name = 'movies/actor_create.html'

    def get_success_url(self):
        return f"{reverse('submission_success')}?type=actor"

class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.filter(status=Movie.APPROVED)
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]