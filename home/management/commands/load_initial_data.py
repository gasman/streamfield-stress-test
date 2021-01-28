import os.path

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError

from wagtail.core.models import Collection
from wagtail.images.models import Image

class Command(BaseCommand):
    def handle(self, *args, **options):
        root_collection = Collection.get_first_root_node()

        try:
            people = Collection.objects.get(name="People")
        except Collection.DoesNotExist:
            people = root_collection.add_child(name="People")

        try:
            breads = Collection.objects.get(name="Breads")
        except Collection.DoesNotExist:
            breads = root_collection.add_child(name="Breads")

        for i in range(1, 7):
            with open(os.path.join(settings.BASE_DIR, 'home', 'example-images', 'person%d.jpg' % i), 'rb') as f:
                Image.objects.create(
                    title="Person %d" % i,
                    file=File(f),
                    collection=people
                )

            with open(os.path.join(settings.BASE_DIR, 'home', 'example-images', 'bread%d.jpg' % i), 'rb') as f:
                Image.objects.create(
                    title="Bread %d" % i,
                    file=File(f),
                    collection=breads
                )
