from django import forms
from .models import Lesson, Grade

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'date']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'value', 'comment']