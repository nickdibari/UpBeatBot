import random
import string

import bs4
import requests

import settings
from libs.api_mock import RequestsMock


class UpBeatBot(object):
    """Source of uplifting media"""

    # List of animals to look for in a message
    animals = [
        'kittens', 'kitten', 'pugs', 'pug', 'cats', 'cat', 'gerbils',
        'gerbil', 'bunnies', 'bunny', 'chipmunks', 'chipmunk', 'dogs',
        'dog', 'otters', 'otter', 'chinchillas', 'chinchilla', 'red pandas',
        'red panda', 'squirrel', 'squirrels'
    ]

    def __init__(self, debug=settings.DEBUG):
        if debug:
            self.request = RequestsMock()
        else:
            self.request = requests

    def get_cute_animal_picture(self, message=None):
        """
        Return a link to a cute picture of an animal. If a message is provided, will try to parse the message for an
        animal we have registered and try to find a picture of the animal. If the message does not contain an animal
        we have registered, or is not provided, will search for a random animal from our choices.
        :param message: (str) Optional message to parse to determine what animal to search for
        :return: (str) Link to an image of a cute animal
        """
        if message:
            animal = self._get_animal_from_message(message)

        else:
            animal = random.choice(self.animals)

        # Get preview page for animal
        preview_html = self.request.get('http://www.cutestpaw.com/?s={0}'.format(animal))

        preview_html.raise_for_status()

        preview_soup = bs4.BeautifulSoup(preview_html.text, 'html.parser')

        # Get random picture from preview page
        photos = preview_soup.select('#photos a')
        choice = random.choice(photos)

        # Get picture page
        picture_html = self.request.get(choice['href'])
        picture_html.raise_for_status()

        picture_soup = bs4.BeautifulSoup(picture_html.text, 'html.parser')

        # Parse picture page for image
        img = picture_soup.select('#single-cute-wrap img')
        link = img[0]['src']

        return link

    def _get_animal_from_message(self, message):
        """
        Given a message (tweet, comment, post, etc.) parse the string to find if the message contains an animal in
        our choices list. If we can't find an animal from our choices in the text, return a random animal from our
        choices list.
        :param message: (str) Text to search for an animal we have registered
        :return: (str) Cute animal to be used for retrieving a cute picture
        """
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
