from numpy.core.fromnumeric import sort
from unittest import TestCase
from game_logic import merge_sort

__author__ = 'advena'


class TestMerge_sort(TestCase):

    def test_merge_sort_on_unsorted_even_list(self):

        to_sort = [4, 5, 2, 6, 2, 1]
        sorted_list = merge_sort(to_sort)

        self.assertEqual(sorted_list, [1, 2, 2, 4, 5, 6])

    def test_merge_sort_on_unsorted_odd_list(self):

        to_sort = [4, 3, 2, 6, 1]
        sorted_list = merge_sort(to_sort)

        self.assertEqual(sorted_list, [1, 2, 3, 4, 6])

    def test_merge_sort_on_empty_list(self):

        to_sort = []
        sorted_list = merge_sort(to_sort)

        self.assertEqual(sorted_list, [])
