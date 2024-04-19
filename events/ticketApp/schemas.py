from ninja import ModelSchema
from typing import Optional
from ticketApp.models import Venue, Event

class VenueSchema(ModelSchema):
  class Meta:
    model = Venue
    fields = ('name', 'street', 'zip_code', 'city')

class EventSchema(ModelSchema): 
  location: Optional[VenueSchema] = None
  
  class Meta:
    model = Event
    fields = ('id', 'title', 'location', 'date_from', 'date_to', 'max_participants', 'active', 'slug')