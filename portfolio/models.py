from django.db import models
from authentication.models import CustomUser

class Project(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=20000, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='projects_files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.user}'


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects_image/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_images')