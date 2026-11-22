from django.contrib.auth import get_user_model
from django import forms
from unfold.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from accounts.models import Profile

UserModel = get_user_model()


class AppUserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email']


class AppUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = UserModel


class RegisterForm(DjangoUserCreationForm):
    class Meta:
        model = UserModel
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth', 'profile_picture']