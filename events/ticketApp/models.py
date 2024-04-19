from django.db import models
from django_extensions.db.fields import AutoSlugField
import uuid

# Create your models here.
class Venue(models.Model):
  name = models.CharField(max_length=200)
  street = models.CharField(max_length=200)
  zip_code = models.IntegerField(null=True)
  city = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.name

class Event(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
  title = models.CharField(max_length=200)
  location = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, blank=True)
  date_from = models.DateTimeField()
  date_to = models.DateTimeField()
  max_participants = models.IntegerField()
  active = models.BooleanField()
  slug = AutoSlugField(populate_from=['title', 'date_from', 'date_to'])

  def __str__(self) -> str:
    return f"{self.title} - {self.location} - {self.date_from.strftime('%c')}"
