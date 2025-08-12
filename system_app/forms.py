from django import forms
from .models import Test

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва тесту:'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис тесту:'}),
        }