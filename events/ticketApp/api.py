from ninja import NinjaAPI
from ticketApp.models import Event, Location
from ticketApp.schemas import EventSchema, LocationSchema

app = NinjaAPI()

@app.get("events/", response=list[EventSchema])
def get_events(request):
  return Event.objects.all()

@app.get("locations/", response=list[LocationSchema])
def get_events(request):
  return Location.objects.all()