from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_by", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("title", "description")
