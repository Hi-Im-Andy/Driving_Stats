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
def max_acceleration():
    '''
    Gets the maximum acceleration of the latest trip taken.

    Args:
        None
    Returns:
        max_acc (float): The maximum acceleration in mph/s over the given trip.
    '''
    acc_tup = localDB.get_acceleration()
    acc = [value[0] for value in acc_tup]
    max_acc = max(acc)
    return max_acc

def min_decceleration():
    '''
    Gets the minimumum decceleraion (quickest breaking time) of the latest trip taken.
    
    Args:
        None
    Returns:
        min_dec (float): The minimum decceleration in mph/s over the given trip.
    '''
    dec_tup = localDB.get_decceleration()
    dec = [value[0] for value in dec_tup]
    min_dec = min(dec)
    return min_dec

def avg_acceleration():
    '''
    Gets the average acceleration time over the course of the trip.

    Args:
        None
    
    Returns:
        avg_acc (float): The average acceleration in mph/s over the given trip.
    '''
    acc_tup = localDB.get_acceleration()
    acc = [value[0] for value in acc_tup]
    avg_acc = float(sum(acc) / len(acc))
    return avg_acc

def avg_decceleration():
    '''
    Gets the average decceleration time over the course of the tip.

    Args:
        None

    Returns:
        avg_dec (float): The average decceleration in mph/s over the given trip.
    '''
    dec_tup = localDB.get_acceleration()
    dec = [value[0] for value in dec_tup]
    avg_dec = float(sum(dec) / len(dec))
    return avg_dec


##############################################################
# Warning and Violation
##############################################################
def warnings():
    '''
    Reads all of the data and notifies the driver of possible recklessness

    Args:
        None

    Returns:
        warnings (int): The number of times that the driver was being reckless
    '''
    # group data by speed limit
    # If the average speed over set speed limit is +-5mph
        # Add warning
    # Check all data, if an data point is +-10mph speed limit
    # and the neighbors are not
    # Add a warning 
    print()



def violations():
    '''
    Reads all of the data and returns the amount of times the driver was significantly reckless

    Args:
        None

    Returns:
        violations (int): The number of times that a driver was significantly reckless
    '''
    # group data by speed limit
    # If the average speed over set speed limit is +-10mph
        # Add warning
    # Check all data, if an data point is +-10mph speed limit
    # and either neighbor is also over
    # Add a violation
    
    print()
    


if (__name__ == "__main__"):
    print("Average Speed: " + str(average_speed()))
    print("Max Speed: " + str(max_speed()))