from django.conf import settings
from django.db import models

class Material(models.Model):
    TYPE_CHOICES = [
        ('file', 'Файл'),
        ('image', 'Зображення'),
        ('link', 'Посилання'),
        ('youtube', 'YouTube Відео'),
    ]

    title = models.CharField(max_length=200, verbose_name="Назва матеріалу")
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Тип")
    file = models.FileField(upload_to='materials/files/', blank=True, null=True, verbose_name="Файл")
    image = models.ImageField(upload_to='materials/images/', blank=True, null=True, verbose_name="Зображення")
    url = models.CharField(blank=True, null=True, verbose_name="Посилання")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата завантаження")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='materials', verbose_name="Автор")

    def __str__(self):
        return self.title