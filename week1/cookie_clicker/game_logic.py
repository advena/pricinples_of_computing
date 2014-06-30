"""
Cookie Clicker Simulator
"""
# import math
# import simpleplot
#
# # Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)
#
# import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._cps = 1.0
        self._time = 0.0
        self._history = [(0.0, None, 0.0, 0.0)]
    def __str__(self):
        """
        Return human readable state
        """
        return ("Cookies: {0} ,CPS: {1}, Time: {2}".format(self.get_cookies(), self.get_cps(), self.get_time()))
    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def set_cookies(self, cookies):
        """
        Sets the current number of cookies to given value
        """

        self._current_cookies = cookies

    def get_total_cookies(self):
        """
        Return total number of cookies produced during simulation
        """

        return self._total_cookies

    def set_total_cookies(self, new_cookies):
        """
        Sets the total number of cookies
        """

        self._total_cookies += new_cookies


    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps

    def set_cps(self, amount):
        """
        Sets the current cookie per second value by given amount
        """

        self._cps = amount

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time

    def set_time(self, new_time):
        """
        Updates the time amount
        """

        self._time = new_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """

        if self.get_cookies() > cookies:
            return 0.0
        cookies_left = cookies - self.get_cookies()
        time_left = cookies_left/self.get_cps()
        return math.ceil(time_left)


    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0
        """

        if time <= 0:
            return
        current_time = self.get_time()
        new_time = current_time + time
        self.set_time(new_time)
        new_cookies = self.get_cookies() + self.get_cps()*time
        self.set_cookies(new_cookies)
        self.set_total_cookies(new_cookies)

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self.get_cookies() < cost:
            return None
        else:
            new_cookies_number = self.get_cookies() - cost
            new_cps = self.get_cps() + additional_cps
            self.set_cookies(new_cookies_number)
            self.set_cps(new_cps)
            self._history.append((self._time, item_name, cost, self.get_total_cookies()))

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to game.
    """


    build_info_clone = build_info.clone()
    items = build_info.build_items()
    cookie_clicker = ClickerState()

    current_time = cookie_clicker.get_time()

    while current_time < duration:
        strategy_output = strategy(cookie_clicker.get_cookies(), cookie_clicker.get_cps(), cookie_clicker.time_until(cookie_clicker.get_cookies()), build_info_clone)
        if not strategy_output:
            cookie_clicker.wait(duration - current_time)
            break
        else:
            pass

    return cookie_clicker



def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left.  Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """


def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    Pick the cheapest option as soon as it is possible to get
    """

    return None

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    Pick the most expensive option as soon as it is possible to get
    """
    return None

def strategy_best(cookies, cps, time_left, build_info):
    """
    Best strategy
    """
    return None

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation with one strategy
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) fo) item in history]
    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

run()


