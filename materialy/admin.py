from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at", "type", "created_by")
    list_filter = ("type", "created_by")
    search_fields = ("title",)
