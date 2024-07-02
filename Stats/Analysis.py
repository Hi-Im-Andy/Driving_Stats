#!/bin/env python3

'''
Used to get metrics from the data (average speed, max acceleration, etc).
'''

import Stats.AwsDB as AwsDB
import Stats.LocalDB as localDB

__author__ = "Andy Hernandez"
__date__ = "6/30/2024"
__status__ = "Development"


def average_speed(lic):
    '''
    Gets the average speed of the latest trip and returns it.

    Args:
        lic (str): The license associated with the driver whose speed we are looking for

    Returns:
        avg (float): The average speed traveled in mph over the given trip.
    '''
    query = '''
    GET * FROM Speed WHERE User_ID = ?
    '''
    data = AwsDB.get_data(query, lic)
    avg = sum(data) / len(data)
    return avg

def max_speed(lic):
    '''
    Gets the maximum speed of the latest trip and returns it.

    Args:
        lic (str): The license associated with the driver whose max speed we are looking for
    
    Returns:
        max (float): The maximum speed traveled in mph over the given trip
    '''
    query = '''
    GET * FROM Trip
    '''
    data = localDB.get_data(query, lic)
    max = max(data)
    return max

