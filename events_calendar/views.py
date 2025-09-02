from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from events_calendar.forms import CalendarForm, EventForm
from events_calendar.models import Calendar, Event
# Create your views here.
class CalendarListView(ListView, LoginRequiredMixin):
    model = Calendar
    template_name = 'events_calendar/calendar_list.html'
    context_object_name = 'calendars'
class CalendarCreateView(CreateView, LoginRequiredMixin):
    model = Calendar
    template_name = 'events_calendar/calendar_create.html'
    form_class = CalendarForm
    success_url = reverse_lazy('calendar_list')
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
class CalendarUpdateView(UpdateView, LoginRequiredMixin):
    model = Calendar
    template_name = 'events_calendar/calendar_form.html'
    # fields = ['name']
    form_class = CalendarForm
    success_url = '/calendars/'
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        # if self.object.created_by != request.user:
        #     return HttpResponseForbidden("Ви не можете редагувати це завдання")
        return super().dispatch(request, *args, **kwargs)
class CalendarDeleteView(DeleteView, LoginRequiredMixin):
    model = Calendar
    template_name = 'events_calendar/calendar_confirm_delete.html'
    success_url = '/calendars/'
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
class CalendarDetailView(DetailView, LoginRequiredMixin):
    model = Calendar
    template_name = 'events_calendar/calendar_detail.html'
    context_object_name = 'calendar'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Отримати всі події, пов'язані з цим календарем
        context['events'] = self.object.events.all()
        return context
class EventCreateView(CreateView, LoginRequiredMixin):
    model = Event
    template_name = 'events_calendar/event_create.html'
    form_class = EventForm
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        calendar_id = self.kwargs.get('pk')
        calendar = Calendar.objects.get(id=calendar_id)
        form.instance.calendar = calendar
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('calendar_detail', kwargs={'pk': self.kwargs['pk']})
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    template_name = 'events_calendar/event_confirm_delete.html'

    def get_success_url(self):
        return reverse('calendar_detail', kwargs={'pk': self.object.calendar.id})

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'events_calendar/event_form.html'
    form_class = EventForm

    def get_success_url(self):
        return reverse('calendar_detail', kwargs={'pk': self.object.calendar.id})



class EventDetailView(DetailView, LoginRequiredMixin):
    model = Event
    template_name="events_calendar/event_detail.html"