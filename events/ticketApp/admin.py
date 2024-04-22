from django.contrib import admin
# Import created models from ticketApplication
from ticketApp.models import Event, Location

# Register Models in Admin Panel to make them editable
admin.site.register(Event)
admin.site.register(Location)

