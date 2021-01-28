import datetime
import json
import os.path
import random

from django.conf import settings
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from django.utils.lorem_ipsum import words

from wagtail.core.models import Page
from wagtail.images.models import Image

from home.models import StreamPage


QUOTES = [
    "How can a nation be great if its bread tastes like Kleenex?",
    "There is not a thing that is more positive than bread.",
    "With a piece of bread in your hand you’ll find paradise under a pine tree.",
    "Good bread is the most fundamentally satisfying of all foods; and good bread with fresh butter, the greatest of feasts.",
    "The smell of good bread baking, like the sound of lightly flowing water, is indescribable in its evocation of innocence and delight.",
    "Two things only the people desire: bread, and the circus games.",
    "If thou tastest a crust of bread, thou tastest all the stars and all the heavens.",
    "Give me yesterday’s Bread, this Day’s Flesh, and last Year’s Cyder.",
]

SLOGANS = [
    "A Better Life, A Better World.",
    "A better way forward.",
    "A diamond is forever.",
    "A little dab'll do ya!",
    "A mind is a terrible thing to waste.",
    "All in or Nothing.",
    "Always Coca-Cola.",
    "Always low prices. Always.",
    "An apple a day keeps the doctor away.",
    "An idea can change your life.",
    "Aren't You Hungry for Burger King now?",
]

VIDEOS = [
    'https://www.youtube.com/watch?v=-7x-QhIUlwE',
    'https://www.youtube.com/watch?v=dx76YPgZviE',
    'https://www.youtube.com/watch?v=cVe3fTL1cPM',
    'https://www.youtube.com/watch?v=Fw8ZDwdyHJQ',
    'https://www.youtube.com/watch?v=tILIeNjbH1E',
]

class Command(BaseCommand):
    def get_testimonial(self):
        names = [
            "Sleve McDichael",
            "Onsen Sweemey",
            "Darryl Archideld",
            "Anatoli Smorin",
            "Rey McSriff",
            "Glenallen Mixon",
            "Mario McRlwain",
            "Raul Chamgerlain",
            "Kevin Nogilny",
            "Tony Smehrik",
            "Bobson Dugnutt",
        ]
        return {
            'photo': random.choice(self.people).id,
            'quote': "<p>%s</p>" % random.choice(QUOTES),
            'attribution': random.choice(names),
        }

    def get_cta(self):
        actions = [
            "Read more", "Donate now", "Take the challenge", "Join today"
        ]
        return {
            'title': random.choice(SLOGANS),
            'image': random.choice(self.breads).id,
            'link_text': random.choice(actions),
            'link': random.choice(self.pages).id,
        }

    def get_image_with_caption(self):
        return {
            'image': random.choice(self.breads).id,
            'caption': "<p>%s</p>" % random.choice(QUOTES),
            'alignment': random.choice(['left', 'right', 'centre'])
        }

    def get_heading(self):
        return {
            'text': random.choice(SLOGANS),
            'size': random.choice(['h2', 'h3', 'h4'])
        }

    def get_carousel(self):
        return [
            {
                'image': random.choice(self.breads).id,
                'caption': "<p>%s</p>" % random.choice(QUOTES),
            }
            for i in range(1, random.randint(8, 10))
        ]

    def get_content(self):
        generators = [
            ('heading', self.get_heading),
            ('paragraph', lambda: "<p>%s</p>" % words(random.randint(50,100))),
            ('carousel', self.get_carousel),
            ('call_to_action', self.get_cta),
            ('video', lambda: random.choice(VIDEOS)),
            ('testimonial', self.get_testimonial),
        ]

        blocks = []
        for i in range(0, random.randint(8, 10)):
            block_type, generator = random.choice(generators)
            blocks.append({'type': block_type, 'value': generator()})

        return blocks

    def get_two_column(self):
        return {
            'left': self.get_content(),
            'right': self.get_content(),
        }

    def get_three_column(self):
        return {
            'left': self.get_content(),
            'middle': self.get_content(),
            'right': self.get_content(),
        }

    def handle(self, *args, **options):
        self.pages = list(Page.objects.filter(depth__gt=1))
        self.people = list(Image.objects.filter(collection__name="People"))
        self.breads = list(Image.objects.filter(collection__name="Breads"))

        generators = [
            ('single_column', self.get_content),
            ('two_column', self.get_two_column),
            ('three_column', self.get_three_column),
        ]

        blocks = []
        for i in range(0, 5):
            block_type, generator = random.choice(generators)
            blocks.append({'type': block_type, 'value': generator()})

        home = Page.objects.get(depth=2)
        stream_page = StreamPage(
            title="Stream page %s" % datetime.datetime.now(),
            body=json.dumps(blocks),
        )
        home.add_child(instance=stream_page)
