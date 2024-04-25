# Richard Repenning - Forms used on the page

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
  """
  Register for a new account.
  """
  email = forms.EmailField(required=True)
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
  """
  Login to an existing account.
  """
  class Meta:
    model = User
    fields = ('username', 'password')

