from ninja import ModelSchema
from typing import Optional
from ticketApp.models import Location, Event

class LocationSchema(ModelSchema):
  class Meta:
    model = Location
    fields = ('name', 'street', 'zip_code', 'city')

class EventSchema(ModelSchema): 
  location: Optional[LocationSchema] = None
  
  class Meta:
    model = Event
    fields = ('id', 'title', 'location', 'date_from', 'date_to', 'max_participants', 'tickets_sold', 'event_status', 'slug')