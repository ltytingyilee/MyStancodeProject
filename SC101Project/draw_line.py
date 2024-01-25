"""
File: draw_line.py
Name: Tina
-------------------------
This file use campy mouse event to
draw GOval and GLine.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constants
SIZE = 10

# Global variables
window = GWindow()
click_count = 1
x = 0
y = 0
circle = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(event):
    """
    Use the odd and even number of mouse clicks to determine
    whether to draw a circle or connect two points into a straight line.
    Odd number of mouse clicks: a circle
    Even number of mouse clicks: connecting last click with this click into a line
    """
    global click_count, circle, x, y
    if click_count % 2 != 0:
        circle = GOval(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
        window.add(circle)
        x = event.x
        y = event.y
    else:
        line = GLine(x, y, event.x, event.y)
        window.add(line)
        window.remove(circle)
    click_count += 1


if __name__ == "__main__":
    main()
