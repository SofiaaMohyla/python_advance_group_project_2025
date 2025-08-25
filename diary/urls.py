from django.urls import path
from . import views

urlpatterns = [
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/<int:pk>/', views.lesson_detail, name='lesson_detail'),
    path('lessons/<int:lesson_id>/grades/new/', views.grade_create, name='grade_create'),
    path('lessons/class/', views.LessonListView.as_view(), name='lesson_list_class'),
    path('lessons/class/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail_class'),
    path('lessons/class/new/', views.LessonCreateView.as_view(), name='lesson_create_class'),
    path('lessons/class/<int:pk>/edit/', views.LessonUpdateView.as_view(), name='lesson_update_class'),
    path('lessons/class/<int:lesson_id>/grades/new/', views.GradeCreateView.as_view(), name='grade_create_class'),
]