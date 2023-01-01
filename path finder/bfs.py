import curses
from curses import color_pair, wrapper
import queue
import time 

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_RED)
    bluered=curses.color_pair(1)

    stdscr.clear()
    stdscr.addstr(5, 5, 'hello world!', bluered)
    stdscr.refresh()
    stdscr.getch()

wrapper(main)


