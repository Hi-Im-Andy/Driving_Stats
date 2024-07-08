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
# Uploading
##############################################################
def upload():
    date = datetime.strftime("%m/%d/%Y")
    print()

if (__name__ == "__main__"):
    print("Average Speed: " + str(average_speed()))
    print("Max Speed: " + str(max_speed()))