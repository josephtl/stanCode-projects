"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3

# Global variables
# graphics = BreakoutGraphics()
# window = graphics.window
# vx = graphics.get_dx()
# vy = graphics.get_dy()
# ball = graphics.ball


def main():
    """
    This program presents a game called breakout.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        if graphics.get_start_status():
            graphics.ball_run()
            graphics.wall_rebound()
            graphics.remove_bricks()
            if graphics.out_of_the_window():
                graphics.restart()
                lives -= 1
                if lives == 0:
                    graphics.lose_game()
                    break
            if graphics.total_bricks == 0:
                graphics.win()
                break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
