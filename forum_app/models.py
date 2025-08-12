from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Post(models.Model):
    title = models.CharField(max_length=250)  
    description = models.TextField(blank=True)  
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if len(self.content.strip()) < 5:
            raise ValidationError("Повідомлення має бути не менше 5 символів")

    def __str__(self):
        return self.title

