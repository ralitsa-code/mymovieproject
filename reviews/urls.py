from django.urls import path
from reviews import views


urlpatterns = [
    path('movies/<int:pk>/review/', views.ReviewCreateView.as_view(),name='review-create'),
]