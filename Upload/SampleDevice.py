#!/bin/env python3

'''
Emmulates a device input with the fake data.
'''

import sys
import time

def fake_all():
    
    i = time.time()
    
    speed = 0
    position = (0, 0)
    speed_limit = 10

    # Setting up the fake device to run for 1 minute of steady acceleration
    while (i < (i + 60)):
        speed +=1
        # Moving in a straight line
        position = (position[0], position[1] + speed)
        # upload 

    # Setting up the fake device to run for 1 minute of steady decceleration.
    while (i < (i + 60)):
        speed -=1
        position = (position[0], position[1] + 1)
        # upload