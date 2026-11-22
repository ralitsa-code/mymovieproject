from django.urls import path

from favorites.views import FavoriteListView, FavoriteAddView, FavoriteDeleteView

urlpatterns = [
    path('', FavoriteListView.as_view(), name='favorites'),
    path('<int:pk>/add/', FavoriteAddView.as_view(), name='favorite_add'),
    path('<int:pk>/remove/', FavoriteDeleteView.as_view(), name='favorite_remove'),
]