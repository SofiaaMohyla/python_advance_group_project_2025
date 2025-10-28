from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline): # TabularInline для компактного вигляду
    model = ProjectImage
    extra = 1  # Кількість порожніх форм для додавання нових зображень

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at') # відображення назви проекту, користувача та дати створення
    search_fields = ('title', 'user__username') # пошук за назвою проекту та ім'ям користувача
    list_filter = ('created_at',)                     # фільтрація за датою створення
    fieldsets = (
        ('Інформація про проєкт', {
            'fields': ('user', 'title', 'desc')
        }),
        ('Файли та зображення', {
            'fields': ('link', 'file')
        }), 
    )
    inlines = [ProjectImageInline]  # Додаємо інлайн для зображень проекту

admin.site.register(ProjectImage)