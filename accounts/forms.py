from django.contrib.auth import get_user_model
from unfold.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm

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

