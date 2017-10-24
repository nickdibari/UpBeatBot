import unittest

from main import get_animal


class TestGetImage(unittest.TestCase):
    """Test that the function returns a suitable search option"""

    def test_chosen_animal_returned(self):
        tweet = 'Hey @upbeatbot send me a dog!'
        animal = get_animal(tweet)

        self.assertEqual(animal, 'dog')

    def test_random_animal_returned_with_text(self):
        tweet = 'Hey @upbeatbot send me a pic!'
        animal = get_animal(tweet)

        # Not really a test, just ensuring *something* is returned
        self.assertTrue(animal)

    def test_random_returned_no_text(self):
        tweet = '@upbeatbot'  # Minimum viable string
        animal = get_animal(tweet)

        # Ditto as above
        self.assertTrue(animal)
