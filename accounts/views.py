from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from sqlalchemy.sql.functions import user

from accounts.forms import RegisterForm
from django.contrib.auth.models import Group

UserModel = get_user_model()

class RegisterAppUserView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        group = Group.objects.get(name='Members')
        self.object.groups.add(group)
        login(self.request, self.object, backend='accounts.backends.EmailBackend')
        return response



