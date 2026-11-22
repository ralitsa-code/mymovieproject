from django.urls import path
from movies import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movies/add/', views.MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/edit/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/add_genre/', views.GenreCreateView.as_view(), name='genre-create'),
    path('movies/add_actor/', views.ActorCreateView.as_view(), name='actor-create'),
    path('movies/add_director/', views.DirectorCreateView.as_view(), name='director-create'),
    path('api/movies/', views.MovieListAPIView.as_view(), name='api-movie-list'),
    path('my-movies/', views.MyMoviesView.as_view(), name='my-movies'),
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('genres/<int:pk>/edit/', views.GenreUpdateView.as_view(), name='genre-update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre-delete'),
]