from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.PollListView.as_view(), name='poll_list'),
    path('<int:poll_id>/question/<int:question_number>/', views.PollDetailView.as_view(), name='poll_detail'),
    path('<int:poll_id>/results/', views.poll_results, name='poll_results'),
    path('<int:poll_id>/retake/', views.retake_poll, name='retake_poll'),
]