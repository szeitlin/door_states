__author__ = 'szeitlin'

#You have 100 doors in a row that are all initially closed.
## you make 100 passes by the doors starting with the first door every time.

## the first time through you visit every door and toggle the door (if the door is closed, you open it, if its open, you close it).
## the second time you only visit every 2nd door (door #2, #4, #6). the third time, every 3rd door (door #3, #6, #9), etc,
# until you only visit the 100th door.
# Question: what state are the doors in after the last pass? which are open which are closed?

class Door(object):

    def __init__(self, state=False, coords=(0,0)):
        self.state = state #False = closed
        self.coords = coords #this will be the location in the final data frame

    def __str__(self):
        msg = self.state, self.coords
        return msg

    def open_door (self):
        self.state = True #True = open
        return self.state

    def close_door (self):
        self.state = False
        return self.state

    def flip_doors(self, door_list = []):
        x =1
        while x <= 2:               #start small
            for x in range(1, 10):
                door_list.append(self.open_door())
            x += 1
        return door_list

import itertools

door_list = range(1,101)

test = Door()

state_1 = [i for i in itertools.repeat(Door, 100)] #idea is to create list of objects, all initially closed

print state_1[:5]

Door.flip_doors(test, state_1)

print door_list[:5]

