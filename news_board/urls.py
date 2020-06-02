from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    PostView, PostCreateView, UpvoteView, UserCreationView, UserLogoutView,
    CommentView, CommentCreateView, home
)


urlpatterns = [
    path('', home),

    path('registration/', UserCreationView.as_view()),
    path('login/', obtain_auth_token),
    path('logout/', UserLogoutView.as_view()),

    path('posts/', PostView.as_view()),
    path('posts/create', PostCreateView.as_view()),
    path('posts/<int:pk>/comments', CommentView.as_view()),
    path('posts/<int:pk>/comments/create', CommentCreateView.as_view()),
    path('posts/<int:post_pk>/upvote', UpvoteView.as_view()),
]
