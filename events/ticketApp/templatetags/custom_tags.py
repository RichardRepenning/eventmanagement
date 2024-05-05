# Richard Repenning - This file is for custom tags used in Django Templates
from django import template
from datetime import timedelta
from django.utils import timezone

register = template.Library()


# used to check if start date of event is 24h before todays date.
# if so the ticket is cancellable
@register.filter(name='is_cancellable')
def is_cancellable(start_date):
    current_datetime = timezone.now()
    return start_date - current_datetime >= timedelta(hours=24)
