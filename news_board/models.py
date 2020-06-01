from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes_number = models.ManyToManyField(User)
    author_name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )

    def __str__(self):
        return self.title

    @property
    def num_upvotes(self):
        return self.upvotes_number.all().count()


class Upvote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Comment(models.Model):
    author_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_comments'
    )
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
