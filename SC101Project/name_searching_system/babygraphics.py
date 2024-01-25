"""
File: babygraphics.py
Name: Tina
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    width_between_lines = (width - GRAPH_MARGIN_SIZE * 2) // len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + width_between_lines * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    top_line = canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                                  GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    bottom_line = canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                     CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                                     CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    for year_index in range(len(YEARS)):
        year_lines = canvas.create_line(get_x_coordinate(CANVAS_WIDTH, year_index), 0,
                                        get_x_coordinate(CANVAS_WIDTH, year_index), CANVAS_HEIGHT, width=LINE_WIDTH)
        year_text = canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, year_index),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=str(YEARS[year_index]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Initialization of the index of COLOR
    color_index = 0

    for name in lookup_names:
        if name in name_data:
            x1 = None
            y1 = None
            for year_index in range(len(YEARS)):
                year = str(YEARS[year_index])
                if year in name_data[name]:
                    rank = name_data[name][year]
                else:
                    rank = MAX_RANK

                # Sets the x and y coordinates of a name in a specific year
                x2 = get_x_coordinate(CANVAS_WIDTH, year_index)
                y2 = GRAPH_MARGIN_SIZE + int(rank) * ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK)

                # Set the color for line and text
                color = COLORS[color_index-len(COLORS)]

                if x1 is not None and y1 is not None:
                    name_line = canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)

                # If the ranking is outside the 1000th, the rank will display '*'
                if rank != MAX_RANK:
                    name_text = canvas.create_text(TEXT_DX+x2, y2, text=str(name)+' ' + rank, anchor=tkinter.SW, fill=color)
                else:
                    name_text = canvas.create_text(TEXT_DX+x2, y2, text=str(name) + '*', anchor=tkinter.SW, fill=color)
                x1 = x2
                y1 = y2

            # Change the color of the next name
            color_index += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
