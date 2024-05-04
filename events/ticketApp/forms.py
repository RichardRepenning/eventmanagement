# Richard Repenning - Forms used on the page

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class SignupForm(UserCreationForm):
    """
    Register for a new account.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    """
    Personal User information
    """

    class Meta:
        model = Profile
        fields = ('street', 'zip_code', 'city', 'birth_date')


class LoginForm(AuthenticationForm):
    """
    Login to an existing account.
    """

    class Meta:
        model = User
        fields = ('username', 'password')
