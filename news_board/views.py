from django.contrib.auth.models import User
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .serializers import (
    PostSerializer, PostCreateSerializer,
    CommentSerializer, CommentCreateSerializer, UserSerializer
)
from .models import Post, Comment


class UserCreationView(generics.CreateAPIView):
    '''
    Used for User registration - set the Token to the User.
    '''
    authentication_classes = []
    permission_classes = []

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLogoutView(generics.GenericAPIView):
    '''
    Used for User logout - delete the Token from the User.
    '''
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_no_content)


class PostView(generics.ListAPIView):
    '''
    Provide a list of all created posts.
    '''
    authentication_classes = []
    permission_classes = []

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    '''
    Creats post.
    '''
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer


class UpvoteView(generics.ListAPIView):
    '''
    Upvotes and unupvotes a particular post by a particular user.
    '''

    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        post_id = self.kwargs['pk']
        post = Post.objects.get(id=post_id)

        if user in post.upvote.all():
            post.upvote.remove(user)
        else:
            post.upvote.add(user)


class CommentView(generics.ListAPIView):
    '''
    Shows all comments to a particular post.
    '''
    authentication_classes = []
    permission_classes = []
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(post_id=self.kwargs['pk'])
        return queryset


class CommentCreateView(generics.CreateAPIView):
    '''
    Creats a comment to a particular post.
    '''
    permission_classes = [IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(post_id=self.kwargs['pk'])
        return queryset


def home(request):
    return HttpResponse("Hello World!")
