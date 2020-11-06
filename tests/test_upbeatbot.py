import unittest

from libs.upbeatbot import UpBeatBot


class TestUpbeatBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.upbeat_bot = UpBeatBot()

    def test_get_cute_animal_picture_with_no_message_returns_random_image(self):
        img_filename = self.upbeat_bot.get_cute_animal_picture()

        # Assert we get an image back
        self.assertTrue('.jpg' in img_filename)

    def test_get_cute_animal_picture_for_message_with_no_animal_in_message_returns_random_image(self):
        img_filename = self.upbeat_bot.get_cute_animal_picture(message='This message has no animal in it')

        # Assert we get an image back
        self.assertTrue('.jpg' in img_filename)

    def test_get_cute_animal_picture_for_message_with_animal_in_message_returns_image_for_animal(self):
        animal = 'cat'
        img_filename = self.upbeat_bot.get_cute_animal_picture(message='Send me a {}'.format(animal))

        # Assert we get an image back from the directory for the animal
        self.assertTrue(animal in img_filename)

    def test_get_animal_from_message_returns_specified_animal(self):
        tweet = 'Hey @upbeatbot send me a dog!'
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        self.assertEqual(animal, 'dog')

    def test_get_animal_from_message_returns_null_if_no_animal_found(self):
        tweet = 'Hey @upbeatbot send me a pic!'
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        self.assertIsNone(animal)

    def test_get_animal_from_message_returns_an_animal_if_multiple_animals_specified(self):
        tweet = 'Hey @upbeatbot send me a dog or a cat!'
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        self.assertTrue(animal in ['dog', 'cat'])
