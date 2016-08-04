#!/usr/bin/python3
import numpy as np
import shutil
import curses
import time
import random


class Game(object):
    """Implements a very basic version of Conway's Game of Life and draws it.
       Linux only.
    """
    def __init__(self, screen=None, width=80, height=24, draw_delay=0.5, block_mode=True):
        # A cell is "alive" if its corresponding matrix entry is True
        self.width = width
        self.height = height
        self.state = np.zeros(dtype=bool, shape=(self.width, self.height))
        self.draw_delay = draw_delay
        self.block_mode = block_mode
        self.screen = screen

    def normalize_coordinates(self, x, y):
        """Takes coordinates that might be off the board and wraps them around"""
        _x = x
        _y = y

        if x > self.width:
            _x = x % self.width
        if y > self.height:
            _y = y % self.height
        return (_x, _y)

    def toggle_live(self, x, y):
        """set cell to live state"""
        self.state[x][y] = True

    def kill(self, x, y):
        """kills a given cell"""
        self.state[x][y] = False

    def toggle(self, x, y):
        """toggle cell's state"""
        _x, _y = self.normalize_coordinates(x, y)
        self.state[_x][_y] = not self.state[_x][_y]

    def clear(self):
        """clears board"""
        self.state = np.zeros(dtype=bool, shape=(self.width, self.height))

    def random(self, threshold=0.5):
        """Generates a random board"""
        self.clear()
        for i in range(self.width):
            for j in range(self.height):
                if random.random() > threshold:
                    self.toggle_live(i, j)

    def step(self):
        """Performs one iteration"""
        temp_state = np.zeros(dtype=bool, shape=(self.width, self.height))
        for i in range(self.width):
            for j in range(self.height):
                neighbors = 0
                is_alive = self.state[i][j]
                # Look at all 8 cells surrounding (i, j)
                # min() and max() handle the cells on the board border
                # min(dimension, n+2) because 0-based indexing (height of 4 ==> max y coordinate of 3)
                for y_border in range(max(0, j-1), min(self.height, j+2)):
                    for x_border in range(max(0, i-1), min(self.width, i+2)):
                        if self.state[x_border][y_border]:
                            neighbors += 1

                # Don't count cell at (i, j)
                neighbors -= int(is_alive)

                if neighbors == 3:
                    temp_state[i][j] = True
                elif neighbors == 2 and is_alive:
                    temp_state[i][j] = True
                else:  # Otherwise we do nothing, already initialized to False
                    pass
        self.state = temp_state

    def step_through(self, steps=10):
        for i in range(steps):
            self.draw()
            self.step()

    def draw(self):
        """draws the board"""

        self.screen.clear()
        for x in range(self.width):
            for y in range(self.height):
                self.draw_cell(x, y)
        time.sleep(self.draw_delay)

    def draw_cell(self, x, y):
        """draws a cell based on its value"""

        if self.state[x][y]:
            if self.block_mode:
                self.screen.addstr(y, x, u'\u2588', curses.color_pair(1))
            else:
                self.screen.addstr(y, x, '*', curses.color_pair(1))

        self.screen.refresh()


def main(stdscr):
    term_size = shutil.get_terminal_size((80, 24))  # use 80x24 as default size

    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN, -1)

    # subtract 1 from lines because curses *really* doesn't like drawing the
    # cursor off the screen.
    game = Game(screen=stdscr, width=term_size.columns, height=term_size.lines-1, draw_delay=0.25, block_mode=True)
    # game = Game(screen=stdscr, width=4, height=5, draw_delay=0.25, block_mode=False)
    game.random(threshold=0.9)
    game.step_through(steps=20)

if __name__ == '__main__':
    curses.wrapper(main)
