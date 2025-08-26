from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.TestListView.as_view(), name='test_list'),
    path('test/<int:pk>/', views.TakeTestView.as_view(), name='test/take_test'),
    path('test/<int:pk>/result/', views.TestResultView.as_view(), name='test/test_result'),
    path('test/create/', views.TestCreateView.as_view(), name='test/test_create'),
    path('test/<int:test_id>/add-question/', views.QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:question_id>/add-choice/', views.ChoiceCreateView.as_view(), name='choice_create'),
]
    