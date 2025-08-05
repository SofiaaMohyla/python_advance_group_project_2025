from django.db import models
from django.conf import settings
from authentication.models import CustomUser

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=255, blank=True, null=True)
    answer_a = models.CharField(max_length=255, blank=True, null=True)
    answer_b = models.CharField(max_length=255, blank=True, null=True)
    answer_c = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='polls')

    def __str__(self):
        return f"{self.question} ({self.created_at})"

