from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView,DetailView

from forum_app.forms import PostForm
from .models import Post, Topic

from rest_framework import generics, permissions
from .serializers import PostSerializer
from rest_framework.pagination import PageNumberPagination

class TopicListView(LoginRequiredMixin,ListView):
    model = Topic
    template_name = 'forum/forum.html'
    context_object_name = 'topics'

class TopicDetailView(LoginRequiredMixin,DetailView):
    model = Topic
    template_name = 'forum/topic_detail.html'
    context_object_name = 'topic'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/post_form.html'
    success_url = reverse_lazy('topic-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['content', 'image', 'file']
    template_name = 'forum/post_form.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'forum/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        return self.get_object().author == self.request.user


class PostPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    

class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPaginator

    def get_queryset(self):
        topic_id = self.kwargs['pk']
        return Post.objects.filter(topic__id=topic_id).order_by('-created_at')
