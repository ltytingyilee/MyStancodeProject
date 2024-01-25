"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

A superclass of all objects that can be displayed on a graphical window.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # a switch that controls whether the ball moves
        self.is_moving = False
        # Initialize our mouse listeners
        onmouseclicked(self.ball_to_move)
        onmousemoved(self.change_paddle_position)
        # Draw bricks
        for row in range(brick_rows):
            for col in range(brick_cols):
                brick_x = row * (brick_width + brick_spacing)
                brick_y = col * (brick_height + brick_spacing) + brick_offset
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                # set the color of bricks
                if col // 2 == 0:
                    self.brick.fill_color = 'red'
                    self.brick.color = self.brick.fill_color
                elif col // 2 == 1:
                    self.brick.fill_color = 'orange'
                    self.brick.color = self.brick.fill_color
                elif col // 2 == 2:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = self.brick.fill_color
                elif col // 2 == 3:
                    self.brick.fill_color = 'green'
                    self.brick.color = self.brick.fill_color
                else:
                    self.brick.fill_color = 'blue'
                    self.brick.color = self.brick.fill_color
                self.window.add(self.brick, x=brick_x, y=brick_y)
        # how many bricks are there on the window
        self.remaining_bricks = brick_rows * brick_cols

    def change_paddle_position(self, event):
        """
        make the paddle move with the mouse
        """
        new_paddle_x = event.x - self.paddle.width / 2
        if 0 <= new_paddle_x <= self.window.width - self.paddle.width:
            self.paddle.x = new_paddle_x

    def ball_to_move(self, event):
        """
        Make the ball move when the mouse is clicked
        """
        if not self.is_moving:
            self.is_moving = True
            self.set_ball_velocity()

    def set_ball_velocity(self):
        """
        Each time the game is clicked to start, the ball can fall in a random direction
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def reset_ball(self):
        """
        Make the ball stop at the initial place
        """
        self.is_moving = False
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2
        self.set_dx(0)
        self.set_dy(0)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def handle_collisions(self):
        """
        Set bounce conditions for collision the paddle and bricks
        """
        # four corners of the ball
        for i in range(2):
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x+self.ball.width*i, self.ball.y+self.ball.height*j)
            if obj is not None:
                # hit the paddle
                if obj is self.paddle:
                    self.set_dy(-self.get_dy())
                    self.ball.move(self.__dx, self.__dy)
                    break
                # hit bricks and remove the bricks
                elif self.ball.y < self.window.height * 0.5 and obj != self.ball:
                    self.set_dy(-self.get_dy())
                    self.window.remove(obj)
                    self.remaining_bricks -= 1
                    break

