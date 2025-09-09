from django.urls import path
from . import views

app_name = "materials"

urlpatterns = [
    path("", views.material_list, name="list"),
    path("material/<int:pk>/", views.material_detail, name="detail"),
    path("material/add/", views.material_create, name="add"),
    path("material/<int:pk>/edit/", views.material_edit, name="edit"),
    path("material/<int:pk>/delete/", views.material_delete, name="delete"),
]
