"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (2,1)
    post-condition: Karel is at (7,2)
    """
    '#''Algorithm'
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()


def go_in():
    """
    pre-condition:karel is at the upper left of the pothole, facing east.
    post-condition:karel is at the pothole, facing south.
    """
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()


def put_99_beepers():
    for i in range(99):
        put_beeper()


def go_out():
    """
    pre-condition:karel is at the pothole, facing south.
    post-condition: karel is at the upper left of the pothole, facing east.
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_around():
    for i in range(2):
        turn_left()





    """
    TODO:
    """


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
