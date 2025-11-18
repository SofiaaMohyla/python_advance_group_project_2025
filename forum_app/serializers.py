from rest_framework import serializers
from .models import Post, Topic

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'content', 'image', 'file', 'created_at', 'topic']


