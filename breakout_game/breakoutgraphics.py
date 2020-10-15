"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window_width - paddle_width) / 2, y=self.window_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius * 2, ball_radius * 2,
                          x=(self.window_width - ball_radius * 2) / 2, y=(self.window_height - ball_radius * 2) / 2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        onmousemoved(self.control)
        onmouseclicked(self.game_start)
        self.__start = False

        # Draw bricks.
        self.total_bricks = 0
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=j * (brick_width + brick_spacing),
                                   y=brick_offset + i * (brick_height + brick_spacing))
                self.brick.filled = True
                if i + 1 <= brick_rows / 5:
                    self.brick.fill_color = 'red'
                elif brick_rows / 5 <= i + 1 <= brick_rows / 5 * 2:
                    self.brick.fill_color = 'orange'
                elif brick_rows / 5 * 2 <= i + 1 <= brick_rows / 5 * 3:
                    self.brick.fill_color = 'yellow'
                elif brick_rows / 5 * 3 <= i + 1 <= brick_rows / 5 * 4:
                    self.brick.fill_color = 'green'
                elif brick_rows / 5 * 4 <= i + 1 <= brick_rows:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)
                self.total_bricks += 1

    # method
    def control(self, mouse):
        """
        Make paddle follows the mouse.
        """
        if self.window.width - self.paddle.width / 2 >= mouse.x >= self.paddle.width / 2:
            self.paddle.x = mouse.x - self.paddle.width / 2
        elif mouse.x > self.window.width - self.paddle.width / 2:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x < self.paddle.width / 2:
            self.paddle.x = 0

    # method
    def game_start(self, mouse):
        """
        Click the mouse to launch the game.
        """
        if not self.__start:
            self.reset_speed()
        self.__start = True

    # method
    def reset_speed(self):
        """
        Reset a new velocity of the ball.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = random.randint(1, INITIAL_Y_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # method
    def ball_run(self):
        """
        Give ball initial velocity.
        """
        self.ball.move(self.__dx, self.__dy)

    # method
    def restart(self):
        """
        Remove the ball and put ball back at the starting point.
        """
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window_width - self.ball_radius * 2) / 2,
                        y=(self.window_height - self.ball_radius * 2) / 2)
        self.__start = False

    def wall_rebound(self):
        """
        Make the ball be able to rebound when it confront the wall.
        """
        if self.ball.x <= 0 or self.ball.x >= self.window.width - self.ball.width:
            self.__dx = -self.__dx

        elif self.ball.y <= 0:
            if self.__dy < 0:
                self.__dy = -self.__dy

    def remove_bricks(self):
        """
        When ball come across a brick, it will rebound and the remove the brick.
        """
        upper_left = self.window.get_object_at(self.ball.x, self.ball.y)
        upper_right = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y)
        lower_left = self.window.get_object_at(self.ball.x, self.ball.y + 2 * self.ball_radius)
        lower_right = self.window.get_object_at(self.ball.x + 2 * self.ball_radius, self.ball.y + 2 * self.ball_radius)

        # come across paddle
        if lower_left is not None and lower_left is self.paddle:
            if self.__dy > 0:
                self.__dy = -self.__dy

        elif lower_right is not None and lower_right is self.paddle:
            if self.__dy > 0:
                self.__dy = -self.__dy

        # removing bricks
        if upper_left is not None and upper_left is not self.paddle:
            self.window.remove(upper_left)
            self.__dy = -self.__dy
            self.total_bricks -= 1

        elif lower_left is not None and lower_left is not self.paddle:
            self.window.remove(lower_left)
            self.__dy = -self.__dy
            self.total_bricks -= 1

        elif upper_right is not None and upper_right is not self.paddle:
            self.window.remove(upper_right)
            self.__dy = -self.__dy
            self.total_bricks -= 1

        elif lower_right is not None and lower_right is not self.paddle:
            self.window.remove(lower_right)
            self.__dy = -self.__dy
            self.total_bricks -= 1

    def lose_game(self):
        """
        GLabel, when run out of lives.
        """
        self.window.clear()
        game_over = GLabel('Game Over!')
        game_over.font = '-70'
        self.window.add(game_over, x=(self.window_width-game_over.width) / 2, y=self.window_height / 2)

    def win(self):
        """
        GLabel, when all the bricks were cleared.
        """
        self.window.clear()
        you_win = GLabel('ALL CLEAR')
        you_win.font = '-70'
        self.window.add(you_win, x=(self.window_width-you_win.width) / 2, y=self.window_height / 2)

    def out_of_the_window(self):
        """
        When ball dropped out of the window.
        """
        if self.ball.y >= self.window.height:
            return True

    def get_start_status(self):
        """
        Boolean
        """
        return self.__start
