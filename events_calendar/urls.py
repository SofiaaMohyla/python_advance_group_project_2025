from django.urls import path

from events_calendar.views import CalendarCreateView, CalendarDeleteView, CalendarDetailView, CalendarListView, CalendarUpdateView, EventCreateView, EventDeleteView, EventDetailView, EventUpdateView

urlpatterns = [
    path('', CalendarListView.as_view(), name='calendar_list'),
    path('<int:pk>/',CalendarDetailView.as_view(), name='calendar_detail'),
    path('<int:pk>/edit/',CalendarUpdateView.as_view(), name='calendar_edit'),
    path('<int:pk>/delete/',CalendarDeleteView.as_view(), name='calendar_delete'),
    path('create/',CalendarCreateView.as_view(), name='calendar_create'),
    path('<int:pk>/create/',EventCreateView.as_view(), name='event_create'),
    path('events/<int:pk>/delete/',EventDeleteView.as_view(), name='event_delete'),
    path('events/<int:pk>/edit/',EventUpdateView.as_view(), name='event_edit'),
    path('events/<int:pk>',EventDetailView.as_view(), name='event_detail'),
]