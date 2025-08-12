from django.urls import path
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('', views.advertisement_list, name='ad_list'),
    path('create/', views.advertisement_create, name='ad_create'),
    path('<int:pk>/edit/', views.advertisement_edit, name='ad_edit'),
    path('<int:pk>/delete/', views.advertisement_delete, name='ad_delete'),
]
