from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["title", "description", "file", "image", "youtube_url", "is_active"]
