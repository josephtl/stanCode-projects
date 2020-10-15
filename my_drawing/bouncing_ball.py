"""
File: bouncing_ball.py
Name: Joseph Liu
-------------------------
This program presents a bouncing ball for three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    ball.filled = True
    ball.fill_color = 'Black'
    window.add(ball)
    onmouseclicked(start)


def start(mouse):
    """
    The ball will start bouncing after clicking the mouse.
    """
    g = 0
    global count
    if ball.x == START_X and ball.y == START_Y and count < 3:
        while ball.x <= window.width:
            ball.move(VX, g)
            g += GRAVITY
            if ball.y + SIZE >= window.height or g == 0:
                g = -g
                g *= REDUCE
            pause(DELAY)
        count += 1
        window.add(ball, START_X, START_Y)


if __name__ == "__main__":
    main()
