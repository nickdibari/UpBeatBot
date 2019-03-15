#! /usr/bin/env python
import random
import string

import bs4
import requests


class UpBeatBot(object):
    """Source of uplifting media"""

    # List of animals to look for in a message
    # Used by _get_animal_from_message
    animals = [
        'kittens', 'kitten', 'pugs', 'pug', 'cats', 'cat', 'gerbils',
        'gerbil', 'bunnies', 'bunny', 'chipmunks', 'chipmunk', 'dogs',
        'dog', 'otters', 'otter', 'chinchillas', 'chinchilla', 'red pandas',
        'red panda', 'squirrel', 'squirrels'
    ]

    def get_cute_animal_picture(self, message=None):
        if message:
            animal = self._get_animal_from_message(message)

        else:
            animal = random.choice(self.animals)

        # Get preview page for animal
        preview_html = requests.get('http://www.cutestpaw.com/?s={0}'.format(animal))

        preview_html.raise_for_status()

        preview_soup = bs4.BeautifulSoup(preview_html.text, 'html.parser')

        # Get random picture from preview page
        photos = preview_soup.select('#photos a')
        choice = random.choice(photos)

        # Get picture page
        picture_html = requests.get(choice['href'])
        picture_html.raise_for_status()

        picture_soup = bs4.BeautifulSoup(picture_html.text, 'html.parser')

        # Parse picture page for image
        img = picture_soup.select('#single-cute-wrap img')
        link = img[0]['src']

        return link

    def _get_animal_from_message(self, message):
        animal = None

        for char in string.punctuation:
            message = message.replace(char, '')

        for word in message.split(' '):
            if word in self.animals:
                animal = word
                break

        if animal is None:
            animal = random.choice(self.animals)

        return animal
