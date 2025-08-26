from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.title} ({self.date})"


class Calendar(models.Model):
    name = models.CharField(max_length=100)
    events = models.ManyToManyField(Event, related_name='calendars')
    image = models.ImageField(upload_to="calendar_image", null = True, blank = True)

    def __str__(self):
        return self.name
