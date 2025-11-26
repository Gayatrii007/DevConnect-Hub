from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from core.models import Post
# Add Comment
class CreateCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')   # URL se le rhe hain
        post = Post.objects.get(id=post_id)    # validate bhi ho gaya
        serializer.save(user=self.request.user, post=post)


# Like / Unlike
class LikePostView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            return Response({"message": "Post liked"})
        else:
            like.delete()
            return Response({"message": "Post unliked"})
