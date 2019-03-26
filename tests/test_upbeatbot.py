import unittest

from libs.upbeatbot import UpBeatBot


class TestUpbeatBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.upbeat_bot = UpBeatBot()

    def test_get_animal_from_message_chosen_animal_returned(self):
        tweet = 'Hey @upbeatbot send me a dog!'
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        self.assertEqual(animal, 'dog')

    def test__get_animal_from_message_random_animal_returned_with_text(self):
        tweet = 'Hey @upbeatbot send me a pic!'
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        # Not really a test, just ensuring *something* is returned
        self.assertTrue(animal)

    def test__get_animal_from_message_random_returned_no_text(self):
        tweet = '@upbeatbot'  # Minimum viable string
        animal = self.upbeat_bot._get_animal_from_message(tweet)

        # Ditto as above
        self.assertTrue(animal)
