from django import forms
from events_calendar.models import Calendar, Event

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Назва календаря"
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control mb-3'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'start_time','end_time']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Назва івенту"
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': "Опис"
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'start_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control mb-3',
                'placeholder': "Час початку"
            }),
            'end_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control mb-3',
                'placeholder': "Час завершення"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'