from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Event
from django.contrib.auth import logout, login, authenticate
from .forms import SignupForm, ProfileForm
from django.db import transaction
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
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
    user_profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
    else:
        # Richard Repenning
        # Check if profile info is missing to display a message in the frontend
        required_fields = ['street', 'zip_code', 'city', 'birth_date']
        profile_incomplete = False

        for field in required_fields:
            if not getattr(user_profile, field):
                profile_incomplete = True
                break

        form = ProfileForm()

        context = {
            'user_profile': user_profile,
            'profile_incomplete': profile_incomplete,
            'form': form
        }

        return render(request, "profile/index.html", context)


@login_required
@transaction.atomic
def update_profile(request):
    user_profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("profile")
        else:
            profile_form = ProfileForm(instance=request.user.profile)
    else:
        data = {'street': user_profile.street, 'zip_code': user_profile.zip_code, 'city': user_profile.city,
                'birth_date': user_profile.birth_date}
        profile_form = ProfileForm(initial=data)
    return render(request, 'profile/update.html', {'profile_form': profile_form})


def testing(request):
    # View for testing different aspects of Django
    # without breaking main project
    template = loader.get_template('template.html')
    context = {
        'genres': ['Techno', 'Rock', 'Pop']
    }
    return HttpResponse(template.render(context, request))
