"""
File: bouncing_ball.py
Name: Tina
-------------------------
This program uses campy mouse event to
control and create the animation of a bouncing ball.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global variable
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
is_bouncing = True
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bounce)


def bounce(mouse):
    """
    The ball falls under the influence of gravity (GRAVITY).
    When the ball hits the bottom of the window, it bounces with 90% gravity.
    The ball returns to its original position after leaving the right side of window.
    Finally, the ball stop moving until the mouse is clicked three times.
    """
    global ball, is_bouncing, count
    ball.filled = True
    window.add(ball)
    vy = 0
    # Control the number of times to stop the ball from bouncing
    if count == 3:
        is_bouncing = False
    else:
        # Stop mouse clicks when the ball bounces
        onmouseclicked(None)
        while True:
            if ball.x + SIZE >= window.width:
                break
            else:
                ball.move(VX, vy)
                vy += GRAVITY
                if ball.y + SIZE >= window.height:
                    vy *= -REDUCE
                    ball.move(VX, vy)
                pause(DELAY)
        ball.x = START_X
        ball.y = START_Y
        count += 1
        onmouseclicked(bounce)


if __name__ == "__main__":
    main()
