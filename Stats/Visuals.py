#!/bin/env python3

'''
Create graphs to visualize the data in the database
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    print()

def speed_limit_overlay(speed, speed_limit):
    '''
    Graphs the speed and speed limit against one another

    Args:
        speed (list): The list of speeds throughout the trip
        speed_limit (list): The list of speed limits throughout the trip

    Returns:
        None
    '''
    print()

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
    print()

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
    print()

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
    print()

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
    print()


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
    print()