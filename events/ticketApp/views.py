from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .models import Event, Ticket
from django.contrib.auth import logout, login, authenticate
from .forms import SignupForm, ProfileForm
from django.db import transaction
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'index.html')


def sign_up(request):
    # Richard Repenning - New User Account creation
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
    # Richard Repenning - Events List
    events = Event.objects.all().values()
    return render(request, "events/index.html", {'events': events})


def event_detail(request, slug):
    # Richard Repenning - Event Detail Page
    event = Event.objects.get(slug=slug)
    if request.user.is_authenticated:
        # Richard Repenning -  Check if user already bought that ticket
        user_ticket = Ticket.objects.filter(user=request.user, event=event).exists()
        return render(request, "events/event.html", {'event': event, 'user_has_ticket': user_ticket})

    return render(request, "events/event.html", {'event': event})


def profile(request):
    # Richard Repenning - Profile Page
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
    # Richard Repenning - Profile Information Update
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


def checkout(request, event_id):
    if request.user.is_authenticated:
        event = get_object_or_404(Event, id=event_id)
        is_ticket = Ticket.objects.filter(user=request.user, event=event).exists()
        if is_ticket and Ticket.objects.filter(user=request.user, event=event).get().status == 'Open':
            return render(request, 'checkout/index.html', {'ticket': Ticket.objects.filter(user=request.user, event=event).get(), 'event': event})

        ticket = Ticket.objects.create(user=request.user, event=event, price=event.base_price)
        return render(request, 'checkout/index.html', {'ticket': ticket, 'event': event})
    else:
        return redirect('login')


def payment(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    ticket = get_object_or_404(Ticket, user=request.user, event=event)
    if ticket:
        ticket.status = Ticket.TicketStatus.PAYED
        ticket.save()
        event.tickets_sold += 1
        event.save()

    return render(request, "checkout/payment.html", {'event': event, 'ticket': ticket})


def tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, "profile/tickets.html", {'tickets': tickets})


def cancel_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    event = ticket.event

    ticket.delete()

    if event:
        event.tickets_sold -= 1
        event.save()

    return render(request, "profile/ticket-cancelled.html", {'ticket': ticket})

