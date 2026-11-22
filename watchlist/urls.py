from django.urls import path

from watchlist.views import WatchlistListView, WatchlistAddView, WatchlistDeleteView


urlpatterns = [
    path('', WatchlistListView.as_view(), name='watchlist'),
    path('<int:pk>/add/', WatchlistAddView.as_view(), name='watchlist_add'),
    path('<int:pk>/remove/', WatchlistDeleteView.as_view(), name='watchlist_remove'),
]