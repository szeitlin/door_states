__author__ = 'szeitlin'

#You have 100 doors in a row that are all initially closed.
## you make 100 passes by the doors starting with the first door every time.

## the first time through you visit every door and toggle the door (if the door is closed, you open it, if its open, you close it).
## the second time you only visit every 2nd door (door #2, #4, #6). the third time, every 3rd door (door #3, #6, #9), etc,
# until you only visit the 100th door.
# Question: what state are the doors in after the last pass? which are open which are closed?

import itertools
import pandas


#let's try doing this with a dataframe, so there can be a list of numbers, then a list of states for each pass

door_list = pandas.DataFrame(range(1,101))

print len(door_list)

state_1 =pandas.DataFrame([i for i in itertools.repeat('closed', 100)])

print len(state_1)

pieces = (door_list, state_1)

door_frame = pandas.concat(pieces, axis = 1)

door_frame.columns = ['numbers', 'state_1']

print door_frame.head()

def door_toggle(x,y):
    '''
    helper function that converts the door state:
    if closed, then open
    if open, then closed
    Let's treat them as boolean, so
    closed = True
    open = False
    bool -> bool
    '''
    if door_frame[y][x] == 'closed':
        door_frame [y+1][x] = 'open'
    elif door_frame[y][x] == 'open':
        door_frame[y+1][x] = 'closed'

    return door_frame[y+1][x]

def loop_doors():
    '''
    increment which doors to toggle
    1. all doors
    2. every other door
    3. every third door
    etc.
    reads df column -> Calls the door_toggle function
    with x as the row, y as the column
    '''
    for i in range(2, 101):
        colname = "state_" + str(i)
        



    return door_toggle