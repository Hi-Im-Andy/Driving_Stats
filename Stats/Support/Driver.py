#!/bin/env python3

'''
The drivers information.
'''

# import googlemaps

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
        # key = "user key"
        # key = input("Google maps api key")
        # maps = googlemaps.Client(key='key
        # send request to geoloocation 
        # Get request in json format and parse to longitude and latitude
        self.longitude = 0
        self.latitude = 0
        return self.longitude, self.latitude


    def get_speed_limit(self):
        '''
        Gets the speed limit at the drivers last known location

        Args:
            self

        Returns:
            speed_limit (float): The speed limit at the last given location
        '''
        # key = "user key"
        # key = input("Google maps api key")
        # maps = googlemaps.Client(key='key')
        # send request to get speed limit at location
        self.update_location()
            # api (self.longitude, self.latitude)
        # Get request in json format and parse to speed limit
        
        self.speed_limit = 0
        return self.speed_limit