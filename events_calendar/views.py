from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from events_calendar.forms import CalendarForm
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
    template_name = 'events_calendar/calendar_create.html'
    form_class = CalendarForm
    success_url = reverse_lazy('calendar_list')
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
class CalendarUpdateView(UpdateView):
    model = Calendar
    template_name = 'events_calendar/calendar_form.html'
    fields = ['name']
    success_url = '/calendars/'
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.created_by != request.user:
            return HttpResponseForbidden("Ви не можете редагувати це завдання")
        return super().dispatch(request, *args, **kwargs)
class CalendarDeleteView(DeleteView):
    model = Calendar
    template_name = 'events_calendar/calendar_confirm_delete.html'
    success_url = '/calendars/'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

