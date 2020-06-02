from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(User)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )

    def __str__(self):
        return self.title

    @property
    def num_upvotes(self):
        return self.upvote.all().count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
