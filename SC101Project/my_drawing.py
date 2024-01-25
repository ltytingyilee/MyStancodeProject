"""
File: my_drawing.py
Name: Tina
----------------------
This file uses the campy module to
draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Boris 小熊波波
    電腦桌子上有個小熊波波(米飛兔的朋友)的小墊子來陪伴我寫作業，
    因此由他來迎接SC101的開始！
    """
    window = GWindow(480, 360, title='Boris 小熊波波')
    # background
    background = GRect(window.width, window.height)
    background.filled = True
    background.color = 'peru'
    background.fill_color = 'peru'
    window.add(background)
    # head
    head = GOval(270, 240)
    head.filled = True
    head.color = 'sienna'
    head.fill_color = 'sienna'
    window.add(head, x=100, y=30)
    # right ear
    r_ear = GArc(100, 150, 265, 225)
    r_ear.filled = True
    r_ear.color = 'sienna'
    r_ear.fill_color = 'sienna'
    window.add(r_ear, x=310, y=46)
    # left ear
    l_ear = GArc(100, 150, 45, 225)
    l_ear.filled = True
    l_ear.color = 'sienna'
    l_ear.fill_color = 'sienna'
    window.add(l_ear, x=70, y=46)
    # right eye
    r_eye = GOval(20, 20)
    r_eye.filled = True
    r_eye.color = 'saddlebrown'
    r_eye.fill_color = 'saddlebrown'
    window.add(r_eye, x=280, y=120)
    # left eye
    l_eye = GOval(20, 20)
    l_eye.filled = True
    l_eye.color = 'saddlebrown'
    l_eye.fill_color = 'saddlebrown'
    window.add(l_eye, x=160, y=120)
    # noise
    noise = GOval(40, 30)
    noise.filled = True
    noise.color = 'saddlebrown'
    noise.fill_color = 'saddlebrown'
    window.add(noise, x=210, y=130)
    # mouth
    r_mouth = GArc(200, 200, 190, 45)
    r_mouth.color = 'saddlebrown'
    window.add(r_mouth, x=230, y=120)
    l_mouth = GArc(200, 200,  300, 45)
    l_mouth.color = 'saddlebrown'
    window.add(l_mouth, x=183, y=120)
    # label
    label = GLabel('Welcome to SC101 ʕ•ᴥ•ʔ')
    label.font = '-40'
    label.color = 'Khaki'
    window.add(label, x=20, y=330)


if __name__ == '__main__':
    main()
