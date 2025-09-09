from django.db import models
from authentication.models import CustomUser

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.title} - {self.date}'

class Grade(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} - {self.value} - {self.lesson}'