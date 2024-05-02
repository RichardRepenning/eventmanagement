from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Event
from django.contrib.auth import logout, login, authenticate
from .forms import SignupForm, ProfileForm

def main(request):
  return render(request, 'index.html')

def sign_up(request):
  if request.method == 'POST':
    form = SignupForm(request.POST )
    # validate the form 
    # https://docs.djangoproject.com/en/5.0/topics/forms/
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('main')
  else:
    form = SignupForm()
  
  return render(request, 'registration/signup.html', {'form': form})

def events(request):
  # Create events Object with all values of Event model
  events = Event.objects.all().values()
  # Load events template
  template = loader.get_template('events.html')
  # Create an object containing the events object
  context = {
    'events': events,
  }
  # Send object to the template
  return HttpResponse(template.render(context, request))

def profile(request):
  user = request.user
  user_information = {
    "first_name": user.first_name,
    "last_name": user.last_name,
    "username": user.get_username(),
    "name": user.get_full_name(),

  }
  return render(request, "profile/index.html", user_information)

# Function for testing different aspects of Django
# without breaking main project
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'genres': ['Techno', 'Rock', 'Pop']
  }
  return HttpResponse(template.render(context, request))