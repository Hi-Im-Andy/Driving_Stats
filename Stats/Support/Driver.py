#!/bin/env python3

'''
The drivers information.
'''

# import googlemaps
# import requests

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
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={self.api_key}"

        # Get request in json format and parse to longitude and latitude
        # response = requests.get(url).json()
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
        # send request to get speed limit at location
        self.update_location()
        # https://roads.googleapis.com/v1/speedLimits?path=38.75807927603043,-9.03741754643809&key='api key'
        # url = f"https://roads.googleapis.com/v1/speedLimits?path={self.latitude},{self.longitude}&key={self.api_key}"
        url = f"https://roads.googleapis.com/v1/speedLimits?path={self.latitude},{self.longitude} &units=MPH &key={self.api_key}"
        # response = requests.get(url)
        # Print the response
        # response_json = response.json()
        # print(response_json)
        
        # Get request in json format and parse to speed limit
        
        self.speed_limit = 0
        return self.speed_limit