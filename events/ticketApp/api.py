from ninja import NinjaAPI
from ticketApp.models import Event, Venue
from ticketApp.schemas import EventSchema, VenueSchema

app = NinjaAPI()

@app.get("events/", response=list[EventSchema])
def get_events(request):
  return Event.objects.all()

@app.get("venues/", response=list[VenueSchema])
def get_events(request):
  return Venue.objects.all()