#!/bin/env python3

'''
The drivers information.
'''

import googlemaps
import googlemaps.client
import requests

__author__ = "Andy Hernandez"
__date__ = "7/10/2024"
__status__ = "Development"

class Driver:
    def __init__(self, name, age, gender, license, car_type):
        self.name = name
        self.age = age
        self.gender = gender
        self.license = license
        self.car_type = car_type
        self.latitude = 0
        self.longitude = 0
        self.speed_limit = 0
        self.api_key = ''

    def set_api_key(self):
        self.api_key = input("API key for google maps: ")

    def get_location(self):
        '''
        Gets the last known longitude and latitude from the users position

        Args:
            None
        
        Returns:
            self.longitude (float): The longitude of where the user is
            self.latitude (float): The latitude of where the user is
        '''
        return self.longitude, self.latitude
    
    def update_location(self):
        '''
        Uses an api call to update the users location and returns it

        Args:
            Self
        
        Returns:
            self.longitude (float): The longitude of where the user is
            self.latitude (float): The latitude of where the user is
        '''
        response = googlemaps.Client(key = self.api_key).geolocate()
        self.latitude = response['location']['lat']
        self.longitude = response['location']['lng']
        return self.longitude, self.latitude


    def get_speed_limit(self):
        '''
        Gets the speed limit at the drivers last known location

        Args:
            self

        Returns:
            speed_limit (float): The speed limit at the last given location
        '''
        self.update_location()
        response = googlemaps.Client(key = self.api_key).speed_limits([self.latitude, self.longitude])
        # Speed limits is no longer being used and is not accepting new clients.
        # 'PERMISSION_DENIED (Speed limits are not available for this project.)
        print(response)
 
        
        self.speed_limit = 0
        return self.speed_limit