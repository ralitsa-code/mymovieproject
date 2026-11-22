from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.forms import RegisterForm, ProfileForm
from django.contrib.auth.models import Group
from accounts.models import Profile

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


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    def get_object(self):
        user = self.request.user
        return user.profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        user = self.request.user
        return user.profile

