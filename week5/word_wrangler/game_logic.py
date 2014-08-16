"""
Student code for Word Wrangler game
"""

import urllib2
# import codeskulptor
# import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """

    output = []
    for element in list1:
        if element not in output:
            output.append(element)

    return output


def compute_intersection(list1, list2):
    """
    Returns one list that contains only elements from list1 and list2 that are the same
    """

    output = []

    for element in list1:
        if element in list2:
            output.append(element)

    return output


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    output = []

    if (len(list1) < len(list2)):
        output = compute_intersection(list1, list2)
    else:
        output = compute_intersection(list2, list1)

    return output


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    to_sort = list1 + list2
    list_lenght = len(to_sort)
    while list_lenght > 0:
        for pos in range(0, list_lenght - 1):
            first = to_sort[pos]
            second = to_sort[pos + 1]
            if first > second:
                to_sort[pos] = second
                to_sort[pos + 1] = first
        list_lenght -= 1

    return to_sort


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    list_length = len(list1)
    if list_length <= 1:
        return list1
    else:

        first_half_list = list1[0:list_length / 2]
        second_half_list = list1[list_length / 2:]
        first_sorted = merge_sort(first_half_list)
        second_sorted = merge_sort(second_half_list)

        return merge(first_sorted, second_sorted)


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    word_length = len(word)
    if word_length < 1:
        return [""]
    else:
        first_char = word[0]
        rest = gen_all_strings(word[1:])
        output = rest[:]
        for word in rest:
            for position in range(len(word)+ 1):
                output.append(word[:position] + first_char + word[position:])
    return output



# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    file_object = file(filename, 'r')

    word_list = [word[:-1] for word in file_object.readlines(-1)]
    file_object.close()
    return word_list


# def run():
#     """
#     Run game.
#     """
#     words = load_words(WORDFILE)
#     wrangler = provided.WordWrangler(words, remove_duplicates,
#                                      intersect, merge_sort,
#                                      gen_all_strings)
#     provided.run_game(wrangler)
#
# # Uncomment when you are ready to try the game
# run()






