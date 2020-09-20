import random
import os
import string

import settings


class UpBeatBot(object):
    """Source of uplifting media"""

    # List of animals we support in our system
    animals = [
        'bunnies', 'bunny', 'cat', 'cats', 'chinchilla', 'chinchillas', 'chipmunk', 'chipmunks',
        'dog', 'dogs', 'kitten', 'kittens', 'otter', 'otters', 'pug', 'pugs', 'squirrel', 'squirrels'
    ]

    def get_cute_animal_picture(self, message=None):
        """
        Return a link to a cute picture of an animal. If a message is provided, will try to parse the message for an
        animal we have registered and try to find a picture of the animal. If the message does not contain an animal
        we have registered, or is not provided, will return a picture for a random animal from our choices.

        :param message: (str) Optional message to parse to determine what animal to search for

        :return: (str) Link to an image of a cute animal
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
        Given a message (tweet, comment, post, etc.) parse the string to find if the message contains an animal in
        our choices list. If we can't find an animal from our choices in the text, return None

        :param message: (str) Text to search for an animal we have registered

        :return: (str | None)
        """
        animal = None

        # Strip punctuation characters from message
        for char in string.punctuation:
            message = message.replace(char, '')

        for word in message.split(' '):
            if word in self.animals:
                return word

        return animal
