#!/bin/env python3

'''
Create graphs to visualize the data in the database
'''

import numpy as np
import matplotlib.pyplot as plt


__author__ = "Andy Hernandez"
__date__ = "7/12/2024"
__status__ = "Development"

##############################################################
# Trip Visuals
##############################################################
def display_speed(speed):
    '''
    Graphs the speed of the trip with speed vs time

    Args:
        speed (list): The list of speeds throughout the trip

    Returns:
        None
    '''
    plt.plot(speed)
    plt.title("Trip Speed")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (mph)")
    plt.show()

def speed_limit_overlay(speed, speed_limit):
    '''
    Graphs the speed and speed limit against one another

    Args:
        speed (list): The list of speeds throughout the trip
        speed_limit (list): The list of speed limits throughout the trip

    Returns:
        None
    '''
    plt.plot(speed)    
    plt.plot(speed_limit, "r--")

    plt.title("Speed and Speed Limit")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (mph)")
    plt.show()

def speed_overlay(speed, max_speed, avg_speed):
    '''
    Graphs the speed with the average and the max speeds shown as well

    Args:
        speed (list): The list of speeds throughout the trip
        max_speed (float): The top speed that was traveled at any given time over the trip
        avg_speed (float): The average speed that was traveled over the trip
    
    Returns:
        None
    '''
    plt.plot(speed)
    plt.plot(max_speed, "r--")
    plt.plot(avg_speed, "g--")

    plt.title("Speed Data")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (mph)")
    plt.show()

def acceleration_overlay(acceleration, max_acceleration, avg_acceleration):
    '''
    Graphs the acceleration along with the max and average

    Args:
        acceleration (list): The list of all of the accelerations during the trip
        max_acceleration (float): The maximum acceleration that was reached during the trip
        avg_acceleration (float): The average acceleration that was reached during the trip

    Returns:
        None
    '''
    plt.plot(acceleration)
    plt.plot(max_acceleration, "r--")
    plt.plot(avg_acceleration, "g--")

    plt.title("Acceleration Data")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (mph/s)")
    plt.show()

def decceleration_overlay(decceleration, min_decceleration, avg_decceleration):
    '''
    Graphs the decceleration along with the min and average

    Args:
        decceleration (list): The list of all of the decceleration during the trip
        min_decceleration (float): The minimum decceleration that was reached during the
        avg_decceleration (float): The average decceleration that was reached during the trip

    Returns:
        None
    '''
    plt.plot(decceleration)
    plt.plot(min_decceleration)
    plt.plot(avg_decceleration)

    plt.title("Decceleration Data")
    plt.xlabel("Time (s)")
    plt.ylabel("Decceleration (mph/s)")
    plt.show()

def overlay(speed, speed_limit, max_acc_point, min_dec_point):
    '''
    Graphs the overview of the trip

    Args:
        speed (list): The list of speeds throughout the trip
        speed_limit (list): The list of the speed limits throughout the trip
        max_acc_point (tuple): The point where the max acceleration was reached
        min_dec_point (tuple): The point where the minimum decceleration was reached

    Returns:
        None
    '''
    plt.plot(speed)
    plt.plot(speed_limit, "r--")
    plt.plot(max_acc_point[0], max_acc_point[1], "g--")
    plt.plot(min_dec_point[0], min_dec_point[1], "b--")
    plt.show()


##############################################################
# AWS Visuals
##############################################################
def speed_compare(speed1, speed2):
    '''
    Graphs the speed of two trips against one another

    Args:
        speed1 (list): The list of speeds for the first trip
        speed2 (list): The list of speeds for the second trip

    Returns:
        None
    '''
    plt.plot(speed1)
    plt.plot(speed2)
    
    plt.title("Speed VS Speed")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (mph)")
    plt.show()


##############################################################
# Main
##############################################################
if (__name__ == "__main__"):
    speed = [10, 11, 12, 13, 16, 12]
    speed_limit = [10, 10, 10, 10, 15, 10]
    # display_speed(speed)
    speed_limit_overlay(speed, speed_limit)