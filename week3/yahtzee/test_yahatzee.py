from unittest import TestCase
from game_logic_yahtzee import *

__author__ = 'advena'


class TestScore(TestCase):
    def test_score_with_six_as_highest_value(self):
        #given
        output = score((1, 1, 1, 3, 6))
        self.assertEqual(6, output)


    def test_score_(self):
        #given
        output = score((6, 6, 5, 5, 5))
        self.assertEqual(15, output)

    def test_score_with_four_twos_one_six(self):
        #given
        output = score((2, 2, 2, 2, 6))
        self.assertEqual(8, output)


class TestExpected_value(TestCase):


    def test_expected_value(self):
        #given
        output = expected_value((2, 1), 6, 3)
        self.assertEqual(output, 6.472222222222222)

