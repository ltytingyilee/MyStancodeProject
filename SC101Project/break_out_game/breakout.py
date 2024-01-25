"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program uses BreakoutGraphics to
create a game called breakout.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    There are one paddle, one ball and several bricks in the window.
    The paddle moves with the mouse, and the ball moves when the mouse click.
    The ball can bounce when it hits the top, left, or right borders of the window and the paddle.
    Also, when it hits a brick, it bounces and removes the brick.
    The termination conditions of the program are:
    1. Clear all bricks
    2. The ball falls out of the bottom of the window NUM_LIVES times
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        graphics.handle_collisions()
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx(-graphics.get_dx())
        if graphics.ball.y <= 0:
            graphics.set_dy(-graphics.get_dy())
        elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            graphics.reset_ball()
            # Game over
            if lives == 0:
                break
        # Game cleared
        if graphics.remaining_bricks == 0:
            break


if __name__ == '__main__':
    main()
