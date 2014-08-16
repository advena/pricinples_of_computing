from unittest import TestCase
from game_logic import gen_all_strings

__author__ = 'advena'


class TestGen_all_strings(TestCase):


    def test_generate_all_strings_two_letter_case(self):

        word = "ab"

        word_list = gen_all_strings(word)

        self.assertEqual(word_list, ["", "b", "a", "ab", "ba"])


    def test_generate_all_strings_three_letter_case(self):

        word = "aab"

        word_list = gen_all_strings(word)

        self.assertEqual(word_list, ["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"])

