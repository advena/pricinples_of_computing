from unittest import TestCase
from game_logic import merge

__author__ = 'advena'


class TestMerge(TestCase):
    def test_merge_on_two_unsorded_not_empty_lists(self):
        list1 = [4, 5, 2, 1]
        list2 = [3, 6, 9, 1]

        self.assertEqual(merge(list1, list2), [1, 1, 2, 3, 4, 5, 6, 9])

    def test_merge_on_empty_lists(self):

        list1 = []
        list2 = []

        self.assertEqual(merge(list1, list2), [])
