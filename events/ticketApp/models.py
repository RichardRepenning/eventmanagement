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

    def __str__(self) -> str:
        return f"{self.title} - {self.location} - {self.date_from.strftime('%c')}"


class Profile(models.Model):
    # Richard Repenning - Profile extends the base User model with additional information
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
    id = ShortUUIDField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('user', 'event')
