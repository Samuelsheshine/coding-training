"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop

    per-condition: karel is at (1,1),facing east.
    post-condition: karel is at (12,1),facing east.
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()
            """
            avoid that karel stop 
            """

def jump():
    """
    pre-con: karel is on the left of the wall, facing east.
    post-con: karel is on the left of the wall, facing east.
    """

    up()
    cross()
    down()


def up():
    """
    pre-condition: karel is on the left of the wall, facing east.
    post-condition:karel is facing north.
    turn_left()
    """
    #facing north
    turn_left()
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    """
    pre-condition:karel is facing north.
    post-condition: karel is at the upper right, facing south.
    :return:
    """

    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition: karel is at the upper right, facing south.
    post-condition: karel is at the bottom of the steeplechase, facing south.
    :return:
    """
    while front_is_clear():
        move()






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
