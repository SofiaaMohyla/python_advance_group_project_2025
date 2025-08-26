from django import forms
from events_calendar.models import Calendar

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