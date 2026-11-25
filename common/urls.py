from django.urls import path
from common import views


urlpatterns = [
    path('submission-success/', views.SubmissionSuccessView.as_view(), name='submission_success'),
]