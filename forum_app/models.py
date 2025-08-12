from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Topic(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if len(self.content.strip()) < 5:
            raise ValidationError("Повідомлення має бути не менше 5 символів")

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
