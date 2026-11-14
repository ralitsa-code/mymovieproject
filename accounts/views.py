from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm


UserModel = get_user_model()

class RegisterAppUserView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')



