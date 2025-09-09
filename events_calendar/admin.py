from django.contrib import admin

from events_calendar.models import Calendar, Event

# Register your models here.
admin.site.register(Event)
admin.site.register(Calendar)