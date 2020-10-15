"""
File: draw_line.py
Name: Joseph Liu
-------------------------
This program allows users drawing line by clicking the mouse.
First click represents the starting point, second click represents the ending point.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
SIZE = 10
window = GWindow()
starting_point = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(start)


def start(mouse):
    """
    When clicking the mouse, it will show an oval as the starting point of a line.
    """
    window.add(starting_point, mouse.x-SIZE/2, mouse.y-SIZE/2)
    onmouseclicked(end)


def end(mouse):
    """
    After clicking second time, it will drawing a line based on starting point and ending point.
    """
    line = GLine(starting_point.x+SIZE/2, starting_point.y+SIZE/2, mouse.x - SIZE / 2, mouse.y - SIZE / 2)
    window.add(line)
    window.remove(starting_point)
    onmouseclicked(start)


if __name__ == "__main__":
    main()
