import os
import random
import re

import settings


class UpBeatBot(object):
    """Source of uplifting media"""

    def __init__(self):
        super().__init__()
        self.animals = []

        # Build list of animals in our inventory from directories in our image directory
        for animal in os.listdir(settings.IMAGE_DIRECTORY):
            self.animals.append(animal)

    def get_cute_animal_picture(self, message=None):
        """
        Return a filepath to a cute picture of an animal. If a message is provided, will try to parse the message for an
        animal we have registered and try to find a picture of the animal. If the message does not contain an animal
        we have registered, or is not provided, will return a picture for a random animal from our choices.

        :param message: (str) Optional message to parse to determine what animal to search for

        :return: (str) Filepath to an image of a cute animal in our inventory
        """
        animal = None

        if message:
            animal = self._get_animal_from_message(message)

        if animal is None:
            animal = random.choice(self.animals)

        # Get a random image for the animal specified
        img_directory = '{}/{}'.format(settings.IMAGE_DIRECTORY, animal)
        img_filename = random.choice(os.listdir(img_directory))

        return '{}/{}'.format(img_directory, img_filename)

    def _get_animal_from_message(self, message):
        """
        Given a message parse the string to find if the message contains an animal in our choices list.
        If we can't find an animal from our choices in the text, return None.

        :param message: (str) Text to search for an animal we have registered

        :return: (str | None)
        """
        animal = None

        # Try to find an animal from our inventory in the message
        find_animal_regex = r'({animals})'.format(animals='|'.join(self.animals))
        ret = re.findall(find_animal_regex, message)

        # re.findall return is a list of matching strings in the message
        # Is an empty list if no match found
        if ret:
            animal = random.choice(ret)

        return animal
