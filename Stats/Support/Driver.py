#!/bin/env python3

'''
The drivers information.
'''

import herepy

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
        self.api_key = input("API key for HERE: ")

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
        here_api = herepy.GeocoderApi(api_key = self.api_key)

        response = here_api.free_form("current location").as_dict()

        self.longitude = response["items"][0]["position"]["lng"]
        self.latitude = response["items"][0]["position"]["lat"]
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
        here_api = herepy.RmeApi(api_key = self.api_key)
        # Need to add a gpx file content
        response = here_api.match_route()
        # response = here_api.speed_limit([self.latitude, self.longitude]).as_dict()
        print(response)
 
        
        self.speed_limit = 0
        return self.speed_limit