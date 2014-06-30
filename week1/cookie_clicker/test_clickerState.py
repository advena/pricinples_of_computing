import unittest
from unittest import TestCase
import game_logic

__author__ = 'advena'


class TestClickerState(unittest.TestCase):
    def test_buy_item(self):
        #given
        cookie_simulation = game_logic.ClickerState()

        cookie_simulation.set_cookies(123.5)
        cookie_simulation.set_total_cookies(123.5)
        cookie_simulation.set_cps(2.3)

        #when
        cookie_simulation.buy_item("cookie factory", 30, 0.7)

        #then

        self.assertEqual((cookie_simulation.get_cookies(),
                          cookie_simulation.get_cps(),
                          cookie_simulation.get_history()), (123.5 - 30, 2.3 + 0.7, [(0.0, None, 0.0, 0.0),
                                                                                     (0.0,
                                                                                      "cookie factory",
                                                                                      30,
                                                                                      123.5)]))

    def test_buy_item_with_zero_cookies(self):
        #given
        cookie_simulator = game_logic.ClickerState()

        #when
        cookie_simulator.buy_item("cookie", 45, 0.3)

        #then
        self.assertEqual(cookie_simulator.get_history(), [(0.0, None, 0.0, 0.0)])


class TestClickerState2(unittest.TestCase):
    def test_wait(self):
        #given
        cookie_simulator = game_logic.ClickerState()

        #when
        cookie_simulator.wait(45)

        #then
        self.assertEqual((cookie_simulator.get_time(), cookie_simulator.get_time()), (45, 45))

    def test_wait_negative_value_for_wait(self):

        #given
        cookie_simulator = game_logic.ClickerState()

        #when
        cookie_simulator.wait(-6)

        #then
        self.assertEqual(cookie_simulator.get_time(), 0.0)




    def test_wait_and_buy(self):
        #given
        cookie_simulator = game_logic.ClickerState()

        #when
        cookie_simulator.wait(45)
        cookie_simulator.buy_item("item", 1.0, 3.5)

        #then
        self.assertEqual(cookie_simulator.get_history(), [(0.0, None, 0.0, 0.0), (45.0, "item", 1.0, 45.0)])

    def test_time_until(self):

        #given
        cookie_simulator = game_logic.ClickerState()

        #when
        cookie_simulator.wait(78)
        cookie_simulator.buy_item('item', 1.0, 1.0)

        #then
        self.assertEqual(cookie_simulator.time_until(22), 0.0)



if __name__ == '__main__':
    #test the grid representation
    unittest.main()


