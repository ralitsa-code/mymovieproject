from django.urls import path
from reviews import views


urlpatterns = [
    path(
        'movies/<int:pk>/review/',
         views.ReviewCreateView.as_view(),
         name='review-create'
         ),
    path(
        'movies/<int:pk>/reviews/<int:review_id>/edit/',
         views.ReviewUpdateView.as_view(),
         name='review-edit'
    ),
    path(
        'movies/<int:pk>/reviews/<int:review_id>/delete/',
        views.ReviewDeleteView.as_view(),
        name='review-delete'
    ),
]