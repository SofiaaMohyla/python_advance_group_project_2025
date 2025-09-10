from django.urls import path
from . import views

app_name = "materials"

urlpatterns = [
    path("", views.material_list, name="list"),
    path("<int:pk>/", views.material_detail, name="detail"),
    path("add/", views.material_create, name="add"),
    path("<int:pk>/edit/", views.material_edit, name="edit"),
    path("<int:pk>/delete/", views.material_delete, name="delete"),
]
