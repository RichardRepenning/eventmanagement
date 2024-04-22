from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.
class Location(models.Model):
  name = models.CharField(max_length=200)
  street = models.CharField(max_length=200)
  zip_code = models.IntegerField(null=True)
  city = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.name

class Event(models.Model):

  class EventStatus(models.TextChoices):
    ACTIVE = "AC", _("Aktiv")
    INACTIVE = "IA", _("Inaktiv")
    CANCELLED = "CA", _("Abgesagt")
    SOLDOUT = "SO", _("Ausverkauft")

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
  title = models.CharField(max_length=200)
  location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
  date_from = models.DateTimeField()
  date_to = models.DateTimeField()
  max_participants = models.IntegerField()
  tickets_sold = models.IntegerField(default=0)
  event_status = models.CharField(max_length=2, choices=EventStatus.choices, default=EventStatus.INACTIVE )
  slug = AutoSlugField(populate_from=['title', 'date_from', 'date_to'])

  def __str__(self) -> str:
    return f"{self.title} - {self.location} - {self.date_from.strftime('%c')}"
