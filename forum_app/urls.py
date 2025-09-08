from django.urls import path
from .views import PostCreateView, PostUpdateView, PostDeleteView, TopicListView,TopicDetailView


urlpatterns = [
    path('', TopicListView.as_view(),name='topic-list'),
    path('topic/<int:pk>/',TopicDetailView.as_view(),name='topic-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
