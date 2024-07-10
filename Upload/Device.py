#!/bin/env python3

'''
Used to get information from the users device.
'''


import googlemaps
# pip install -U googlemaps
# Use roads api to get speed limit
# Possibly use geolocation api to get the longitude and latitude


__author__ = "Andy Hernandez"
__date__ = "07/09/2024"
__status__ = "Development"

def get_position():
    '''
    Gets the longitude and latitude from the users position

    Args:
        None

    Returns:
        longitude (float): The longitude of where the user is
        latitude (float): The latitude of where the user is
    '''
    longitude = 1
    latitude = 0

    return longitude, latitude

def get_limit():
    '''
    Gets the speed limit of the location where the user is

    Args:
        None

    Returns:
        speed_limit (int): The speed limit at the current location
    '''
    speed_limit = 0

    return speed_limit