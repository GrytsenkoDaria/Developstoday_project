from django.core.management.base import BaseCommand
from news_board.models import Upvote


class Command(BaseCommand):
    def handle(self, *args, **options):
        Upvote.objects.all().delete()
