from unittest import TestCase
import game_logic

__author__ = 'advena'


class TestRemoveDuplicates(TestCase):
    def test_remove_duplicates(self):
        list_of_duplicates = ["aaa", "aaa", "bbb"]
        list_without_duplicate = remove_duplicates(list_of_duplicates)
        self.assertEqual(list_without_duplicate, ["aaa", "bbb"])



