from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializer import PostSerializer, CommentSerializer

# Create your views here.
from comments.models import Comment


@api_view(http_method_names=['GET'])
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    serializer = PostSerializer(post_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['GET'])
def comments(request):
    post_list = Comment.objects.all().order_by('-created_time')
    serializer = CommentSerializer(post_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
