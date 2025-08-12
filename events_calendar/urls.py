from django.urls import path

from events_calendar.views import CalendarCreateView, CalendarDeleteView, CalendarDetailView, CalendarListView, CalendarUpdateView

urlpatterns = [
    path('calendars/',CalendarListView.as_view(), name='calendar_list'),
    path('calendars/<int:pk>/',CalendarDetailView.as_view(), name='calendar_detail'),
    path('calendars/<int:pk>/edit/',CalendarUpdateView.as_view(), name='calendar_edit'),
    path('calendars/<int:pk>/delete/',CalendarDeleteView.as_view(), name='calendar_delete'),
    path('calendars/create/',CalendarCreateView.as_view(), name='calendar_create'),
]