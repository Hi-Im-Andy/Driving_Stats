#!/bin/env python3

'''
Used to get metrics from the data (average speed, max acceleration, etc).
'''

from datetime import datetime
import AwsDB as AwsDB
import LocalDB as localDB


__author__ = "Andy Hernandez"
__date__ = "6/30/2024"
__status__ = "Development"

##############################################################
# Speed
##############################################################
def average_speed():
    '''
    Gets the average speed of the latest trip and returns it.

    Args:
        None

    Returns:
        avg (float): The average speed traveled in mph over the given trip.
    '''
    speed_tup = localDB.get_speed()
    speed = [value[0] for value in speed_tup]
    avg = float(sum(speed) / len(speed))
    return avg

def max_speed():
    '''
    Gets the maximum speed of the latest trip and returns it.

    Args:
        None
    
    Returns:
        max_speed (float): The maximum speed traveled in mph over the given trip
    '''
    speed_tup = localDB.get_speed()
    speed = [value[0] for value in speed_tup]
    max_speed = max(speed)
    return max_speed


##############################################################
# Acceleration and Decceleration
##############################################################
def acceleration():
    
    print()

def decceleration():
    print()


##############################################################
# Uploading
##############################################################
def upload():
    date = datetime.strftime("%m/%d/%Y")
    print()

if (__name__ == "__main__"):
    print("Average Speed: " + str(average_speed()))
    print("Max Speed: " + str(max_speed()))