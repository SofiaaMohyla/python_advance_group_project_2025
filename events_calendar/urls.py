from django.urls import path

from events_calendar.views import CalendarDeleteView, CalendarDetailView, CalendarListView, CalendarUpdateView

urlpatterns = [
    path('calendars/',CalendarListView.as_view(), name='calendar_list'),
    path('calendars/<ink:pk>/',CalendarDetailView.as_view(), name='calendar_detail'),
    path('calendars/<ink:pk>/edit/',CalendarUpdateView.as_view(), name='calendar_edit'),
    path('calendars/<ink:pk>/delete/',CalendarDeleteView.as_view(), name='calendar_delete'),
]