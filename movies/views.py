from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from movies.models import Movie
from movies.forms import MovieCreateForm, MovieDeleteForm
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'movies/home.html'

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        approved_movies = super( ).get_queryset().filter(status=Movie.APPROVED)
        return approved_movies

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieCreateForm
    template_name = 'movies/movie_create.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        current_user = self.request.user
        form.instance.user = current_user
        return super().form_valid(form)


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
    success_url = reverse_lazy('home')

    def get_queryset(self):
        user_movies = super( ).get_queryset().filter(user=self.request.user)
        return user_movies


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    form_class = MovieDeleteForm
    template_name = 'movies/movie_delete.html'
    success_url = reverse_lazy('home')


    def get_queryset(self):
        user_movies = super( ).get_queryset().filter(user=self.request.user)
        return user_movies
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
