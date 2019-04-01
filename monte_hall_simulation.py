"""
This program simulates the Monte Hall Problem and outputs the probabilies
of switching vs not switching the doors.

Author: Sander Shi
Date: 04/01/2019
"""

import random


class MonteHall(object):
    """
    The Monte Hall class initializes a game by picking a winning door in
    a random manner.
    """

    def __init__(self):
        self.doors = {0, 1, 2}
        self.selection = None
        self.restart()

    def restart(self):
        """
        This function reinitializes the game.
        """
        self.winning_door = random.choice(tuple(self.doors))
        self.selection = None

    def select(self, door):
        """
        This function selects a door and marks it in the state.
        """
        self.selection = door if door in self.doors else None

    def reveal(self):
        """
        This function reveals a door that is not winning amongst the two
        unselected doors.
        """
        if self.selection is None:
            return None
        doors = self.doors - {self.selection, self.winning_door}
        return random.choice(tuple(doors))

    def win(self):
        """
        This function returns true if the selection is winning.
        """
        return self.selection == self.winning_door

    def switch(self):
        """
        This function switches the selection
        """
        self.selection = list(self.doors - {self.reveal(), self.selection})[0]


def main():
    """
    This function runs 10000 simulations on switching versus not switching.
    """
    iterations = 10000
    choices = [0, 1, 2]
    game = MonteHall()

    # Do not switch
    win_count = 0
    for i in range(iterations):
        game.restart()
        door = random.choice(choices)
        game.select(door)
        if game.win():
            win_count += 1
    print("No switching:", win_count / iterations)

    win_count = 0
    for i in range(iterations):
        game.restart()
        door = random.choice(choices)
        game.select(door)
        game.switch()
        if game.win():
            win_count += 1
    print("Switching:", win_count / iterations)


if __name__ == "__main__":
    main()
