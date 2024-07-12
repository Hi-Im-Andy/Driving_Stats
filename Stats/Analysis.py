#!/bin/env python3

'''
Used to get metrics from the data (average speed, max acceleration, etc).
'''

import Stats.LocalDB as localDB

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
    # Gets the acceleration from the data base
    acc_tup = localDB.get_acceleration()
    acc = [value[0] for value in acc_tup]
    # Removes all 0 values in the list
    acc = [value for value in acc if value != 0]
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
    dec = [value for value in dec != 0]
    avg_dec = float(sum(dec) / len(dec))
    return avg_dec

##############################################################
# Comparisons
##############################################################
def acceleration_comparison(car_type, acc_time):
    '''
    Compares the input car type and average acceleration and returns the delta from average.
    
    Args:
        car_type (str): The car type determines what time should be compared
        acc_time (float): Given acceleration for the trip that will be compared to the overall average

    Returns:
        acc_delta (float): Acceleration difference for the given vehicle type and the given acceleration
    '''
    # Query the local database for the all of the accelerations
    # Keep only the accelerations after a speed == 0 for x number of seconds
    # All of those accelerations should be averaged
    # Compare the given acceleration to the average acceleration
    print()

def decceleration_comparison(car_types, dec_time):
    '''
    Compares the input car type average decceleration and returns the delta from average.

    Args:
        car_type (str): The car type determines what time should be compared
        dec_time (float): Given decceleration for the trip that will be compared to the overall average

    Returns:
        dec_delta (float): Decceleration difference for the given vehicle type and the given decceleration
    
    '''
    # Query the local database for the all of the deccelerations
    # Keep onlt the deccelerations before any speed == 0 for x number of seconds prior
    # All of those deccelerations should be averaged
    # Compare the given decceleration to the average decceleration

    print()

if (__name__ == "__main__"):
    print("Average Speed: " + str(average_speed()))
    print("Max Speed: " + str(max_speed()))