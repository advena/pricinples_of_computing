from unittest import TestCase
from game_logic import remove_duplicates

__author__ = 'advena'


class TestRemove_duplicates(TestCase):
    def test_remove_duplicates(self):
        list_of_duplicates = ["aaa", "aaa", "bbb"]
        list_without_duplicate = remove_duplicates(list_of_duplicates)
        self.assertEqual(list_without_duplicate, ["aaa", "bbb"])
