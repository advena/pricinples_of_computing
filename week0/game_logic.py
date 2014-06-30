"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random
import unittest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """


    result_line = [number for number in line if number != 0]
    result_line.extend([number for number in line if number == 0])



    for pos in range(0, len(line) - 1):
       if result_line[pos] == result_line[pos + 1]:
            result_line[pos] = result_line[pos] * 2
            result_line.pop(pos + 1)
            result_line.append(0)
    return result_line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.height = grid_height
        self.width = grid_width
        self.twos = 0
        self.grid = dict([((x, y), 0) for x in range(self.height) for y in range(self.width)])
        #compute directions dictionary
        self.directions = self.create_directions(self.height, self.width)


    def create_directions(self, height, width):
        """
        Returns first tiles for each directions
        ex.  UP all tiles in first row: (0,1), (0,2), ... (0, width)
        """

        directions = {}
        up = []
        down = []
        left =[]
        right = []
        #first add UP and DOWN
        for pos in range(0, width):

            up.append((0,pos))
            down.append((height-1, pos))
        #now LEFT and RIGHT
        for pos in range(0, height):
            left.append((pos,0))
            right.append((pos, width-1))

        directions[UP] = up
        directions[DOWN] = down
        directions[LEFT] = left
        directions[RIGHT] = right


        return directions





    def get_grid(self):
        """
        Returns the grid
        """

        return self.grid

    def reset(self):
        """
        Reset the game so the grid is empty.
        """

        for key in self.grid.keys():
            if self.grid[key] != 0:
                self.grid[key] = 0


    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str_repr = "["

        for row in range(self.get_grid_width()):
            current_row = "["
            for column in range(self.get_grid_height()):
                current_row += str(self.get_tile(row, column))
                current_row += ", "
            current_row = current_row[:-2] + "],\n"
            grid_str_repr += current_row

        grid_str_repr = grid_str_repr[:-2] + "]"

        return grid_str_repr

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height


    def get_grid_width(self):
        """
        Get the width of the board.
        """

        return self.width


    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        has_changed = False
        to_merge = []
        #get the staring points
        starting_points = self.directions[direction]
        #get the offset for given direction
        offset = OFFSETS[direction]
        #now iterate over each staring point and append to to_merge all consecutive tiles for that starting point
        current_tile = starting_points[0]
        for start in starting_points:
            tiles = []
            end = len(starting_points)
            while end >= 0:
                value = self.grid[current_tile]
                tiles.append(value)
                current_tile = (current_tile[0] + offset[0], current_tile[1] + offset[1])
                end -= 1
            to_merge.append(tiles)

        #merge each line
        merged = []
        for line in to_merge:
            merged.append(merge(line))

        #now iterate over each line and assign proper value to the proper tile
        #initialize pos to keep track proper value for each tile
        pos = 0
        for start in starting_points:
            end = len(starting_points)
            row = start[0]
            col = start[1]
            current_tile = start
            while end > 3:
                value = merged[row][col]
                self.set_tile(row, col, value)
                row += offset[0]
                col += offset[1]
                end -= 1








    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #get all empty tiles
        temp = []
        for key in self.grid.keys():
            if self.grid[key] == 0:
               temp.append(key)

        #randomly get the tile for new value
        new_tile_pos = random.randint(0, len(temp)-1)
        new_tile = temp[new_tile_pos]
        #check if it should be 2 or 4
        if self.twos < 9:
            self.set_tile(new_tile[0], new_tile[1], 2)
            self.twos += 1
        else:
            self.set_tile(new_tile[0], new_tile[1], 4)
            self.twos = 0

        return new_tile


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """

        self.grid[(row, col)] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[(row, col)]

# class SimpleGridTest(unittest.TestCase):
#     """
#     This is the grid tester
#     """
#
#
#     def test_grid1(self):
#         """
#         Define simple 3x3 grid
#         """
#
#         grid = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
#                 (1, 0): 0, (1, 1): 0, (1, 2): 0,
#                 (2, 0): 0, (2, 1): 0, (2, 2): 0}
#
#         self.assertEqual(grid, TwentyFortyEight(3, 3).get_grid())
#
#     def test_grid2(self):
#         """
#         Define the multidimension grid 4x6
#         """
#
#         grid = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0,
#                 (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 0,
#                 (2, 0): 0, (2, 1): 0, (2, 2): 0, (2, 3): 0,
#                 (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0,
#                 (4, 0): 0, (4, 1): 0, (4, 2): 0, (4, 3): 0,
#                 (5, 0): 0, (5, 1): 0, (5, 2): 0, (5, 3): 0}
#
#         self.assertEqual(grid, TwentyFortyEight(4, 6).get_grid())
#
#
# class MergeTest(unittest.TestCase):
#     """
#     Tester for the merge function
#     """
#
#     def test_merge1(self):
#         """
#         Define the list to merge
#         """
#
#         to_merge = [8, 32, 8, 0]
#         self.assertEqual(to_merge, merge([8, 16, 16, 8]))
#
#     def test_merge2(self):
#         """
#         Define the list with nozero at the first index
#         """
#
#         to_merge = [2, 4, 0, 0]
#         self.assertEqual(to_merge, merge([2, 4, 0, 0]))
#
#     def test_merge3(self):
#         """
#         Define the list with zero between the numbers
#         """
#
#         to_merge = [8, 2, 4, 8, 0, 0, 0, 0]
#         self.assertEqual(to_merge, merge([8, 0, 0, 2, 4, 0, 0, 8]))
#
#
#     def test_merge4(self):
#         """
#         Define test list with all the same even number elements
#         """
#
#         to_merge = [4, 4, 0, 0]
#         self.assertEqual(to_merge, merge([2, 2, 2, 2]))
#
#     def test_merge5(self):
#         """
#         Define the list with
#         """
#
#         to_merge = [4, 4, 2, 0, 0]
#         self.assertEqual(to_merge, merge([2, 2, 2, 2, 2]))
#
#     def test_merge6(self):
#         """
#         Defiue the list to merge
#         """
#
#         to_merge = [4, 4, 0, 0]
#         self.assertEqual(to_merge, merge([2, 0, 2, 4]))

class SimpleGameTester(unittest.TestCase):

    # def test_gameCreate(self):
    #
    #     game = TwentyFortyEight(3,5)
    #     value = game.get_grid()[game.new_tile()]
    #
    #     game.set_tile(0,0, 2)
    #     game.set_tile(2,4, 2)
    #     game.move(UP)
    #     self.assertEqual(value, 2)
    #     self.assertEqual(game.get_grid_height(), 3)
    #     self.assertEqual(game.get_grid_width(), 5)
    #     self.assertEqual(game.get_tile(0,0), 2)
    #     self.assertEqual(game.get_tile(2,4), 2)

    def test_gameMovement(self):

        game = TwentyFortyEight(4,4)
        game.set_tile(0, 0, 2)
        game.set_tile(1, 1, 2)
        game.set_tile(2, 2, 2)
        game.set_tile(3, 3, 2)

        out_game_grid = "[[2, 0, 0, 0],\n[0, 2, 3, 0],\n[0, 0, 2, 4],\n[0, 0, 0, 5]]"
        # self.assertEqual(out_game_grid, game.__str__())
        game.move(UP)
        out_game_grid_after_move = "[[2,2,2,2],\n[0,0,0,0],\n[0,0,0,0],\n[0,0,0,0]]"
        self.assertEqual(out_game_grid_after_move, game.__str__())







#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
if __name__ == '__main__':
    #test the grid representation
    unittest.main()