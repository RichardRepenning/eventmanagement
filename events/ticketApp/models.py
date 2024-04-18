from django.db import models

# Create your models here.
class Venue(models.Model):
  name = models.CharField(max_length=200)
  street = models.CharField(max_length=200)
  zip_code = models.IntegerField(null=True)
  city = models.CharField(max_length=100)

class Event(models.Model):
  title = models.CharField(max_length=200)
  location = models.ForeignKey(Venue, on_delete=models.CASCADE)
  date_from = models.DateField()
  date_to = models.DateField()
  max_participants = models.IntegerField()
  active = models.BooleanField()
