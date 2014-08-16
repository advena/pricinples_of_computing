from unittest import TestCase
from game_logic import intersect

__author__ = 'advena'


class TestIntersect(TestCase):

    def test_lists_without_duplicates(self):
        list1 = ["a", "b", "c"]
        list2 = ["d", "m"]

        self.assertEqual(intersect(list1, list2), [])

    def test_lists_with_duplicates(self):
        list1 = [1, 2, 3, 5]
        list2 = [1, 4, 6, 2, 43, 5]

        self.assertEqual(intersect(list2, list1), [1, 2, 5])
