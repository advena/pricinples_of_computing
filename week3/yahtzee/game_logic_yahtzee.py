"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = [()]
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return sorted(answer_set)





def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    current_hand = {}
    for dice in hand:
        if not current_hand.get(dice):
            current_hand[dice] = dice
        else:
            current_hand[dice] += dice

    #compute the current score for each dice

    return max(current_hand.values())


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """

    outcome = ()
    for die in range(1, num_die_sides + 1):
        outcome +=(die, )
    possible_outcomes = gen_all_sequences(outcome, num_free_dice)
    output = 0
    for single_output in possible_outcomes:
        current_score = score(single_output + held_dice)
        output += current_score

    return output/(len(possible_outcomes)*1.0)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """

    mask = sorted(gen_all_sequences((1,0), len(hand)))
    answer_set = []
    for current_mask in mask:
        temp = []
        for indx in range(len(current_mask)):
            if current_mask[indx] == 1:
                temp.append(hand[indx]);
        answer_set.append(tuple(temp))
    return set(answer_set)





def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    all_holds = gen_all_holds(hand)
    expected_values = {}
    for hold in all_holds:
        num_free_dice = len(hand) - len(hold)
        current_expexted_value = expected_value(hold, num_die_sides, num_free_dice)
        expected_values[current_expexted_value] = hold

    max_value = max(expected_values.keys())
    return tuple((max_value, expected_values[max_value]))


# def run_example():
#     """
#     Compute the dice to hold and expected score for an example hand
#     """
#     # num_die_sides = 6
#     # hand = (1, 1, 1, 5, 6)
#     # hand_score, hold = strategy(hand, num_die_sides)
#     # print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
#     print strategy((1,), 6)
#     print expected_value((1, ), 6, 5)
# run_example()


# import poc_holds_testsuite
# poc_holds_testsuite.run_suite(gen_all_holds)







