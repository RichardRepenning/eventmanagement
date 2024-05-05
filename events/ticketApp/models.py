# This file contains the models for the project

from django.db import models
from django_extensions.db.fields import AutoSlugField
from shortuuidfield import ShortUUIDField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


# Create your models here.

class Location(models.Model):
    # Richard Repenning - Location Class
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zip_code = models.IntegerField(null=True)
    city = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    # Richard Repenning - Event Class
    class EventStatus(models.TextChoices):
        ACTIVE = "AC", _("Aktiv")
        INACTIVE = "IA", _("Inaktiv")
        CANCELLED = "CA", _("Abgesagt")
        SOLDOUT = "SO", _("Ausverkauft")

    id = ShortUUIDField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    date_from = models.DateTimeField()
    description = models.TextField(blank=True)
    date_to = models.DateTimeField()
    max_participants = models.IntegerField()
    tickets_sold = models.IntegerField(default=0)
    event_status = models.CharField(max_length=2, choices=EventStatus.choices, default=EventStatus.INACTIVE)
    slug = AutoSlugField(populate_from=['id'])
    base_price = models.DecimalField(max_digits=5, decimal_places=2, default=999.99)

    def __str__(self) -> str:
        return f"{self.title} - {self.location} - {self.date_from.strftime('%c')}"

    def buy_ticket(self, user):
        ticket = Ticket.objects.create(user=user, event=self, price=self.base_price)
        return ticket


class Profile(models.Model):
    # Richard Repenning - Profile extends the base User model with additional information
    # https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=200, blank=True)
    zip_code = models.IntegerField(default=0, blank=True)
    city = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    # define signals so that the profile is updated/created whenever the User gets updated/created
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"


class Ticket(models.Model):
    class TicketStatus(models.TextChoices):
        PAYED = _("Payed")
        OPEN = _("Open")
        CANCELED = _("Canceled")

    id = ShortUUIDField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(choices=TicketStatus.choices, default=TicketStatus.OPEN, max_length=100)

    class Meta:
        # Richard Repenning - Only one ticket per user and event
        unique_together = ('user', 'event')


class Checkout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)

    @classmethod
    def create_checkout(cls, user, ticket):
        # Check, if a checkout already exists for this user
        existing_checkout = cls.objects.filter(user=user).first()
        if existing_checkout:
            # Falls ein Checkout bereits existiert, aktualisiere das Ticket im bestehenden Checkout
            existing_checkout.ticket = ticket
            existing_checkout.save()
            return existing_checkout
        else:
            # Falls kein Checkout existiert, erstelle einen neuen Checkout
            return cls.objects.create(user=user, ticket=ticket)
