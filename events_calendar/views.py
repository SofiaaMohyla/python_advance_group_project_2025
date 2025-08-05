from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from events_calendar.models import Calendar
# Create your views here.
class CalendarListView(ListView):
    model = Calendar
    template_name = 'events_calendar/calendar_list.html'
    context_object_name = 'calendars'
class CalendarDetailView(DetailView):
    model = Calendar
    template_name = 'events_calendar/calendar_detail.html'
    context_object_name = 'calendar'
class CalendarCreateView(CreateView):
    model = Calendar
    template_name = 'events_calendar/calendar_form.html'
    fields = ['name']
    success_url = '/calendars/'
class CalendarUpdateView(UpdateView):
    model = Calendar
    template_name = 'events_calendar/calendar_form.html'
    fields = ['name']
    success_url = '/calendars/'
class CalendarDeleteView(DeleteView):
    model = Calendar
    template_name = 'events_calendar/calendar_confirm_delete.html'
    success_url = '/calendars/'
