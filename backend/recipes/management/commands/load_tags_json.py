import json

from django.core.management.base import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("recipes/data/tags.json") as json_file:
            data = json.load(json_file)
            for tag in data:
                db = Tag(
                    name=tag["name"], color=tag["color"], slug=tag["slug"]
                )
                db.save()
