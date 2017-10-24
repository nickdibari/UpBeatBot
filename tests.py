import unittest
import mock

from main import GetImage


class TestGetImage(unittest.TestCase):
    """Test that the function returns a suitable search option"""
    def test_chosen_animal_returned(self):
        
