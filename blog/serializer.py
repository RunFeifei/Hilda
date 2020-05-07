from django.contrib.auth.models import User
from rest_framework import serializers

from blog.models import Category, Post, Tag
from comments.models import Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name'
        ]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name'
        ]


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer
    author = UserSerializer
    tags = TagSerializer

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'created_time',
            'modified_time',
            'excerpt',
            'category',
            'author',
            'tags',
        ]


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer

    class Meta:
        model = Comment
        fields = [
            'id',
            'name',
            'email',
            'url',
            'text',
            'created_time',
            'post',
        ]
