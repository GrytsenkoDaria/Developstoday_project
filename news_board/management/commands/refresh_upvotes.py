from django.core.management.base import BaseCommand
from news_board.models import Post


class Command(BaseCommand):
    def handle(self, *args, **options):
        posts = Post.objects.all()
        for post in posts:
            post.upvote.clear()
