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
        self.warnings = 0
        self.violations = 0
        self.speed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def reset(self):
        '''
        Sets the driving info back to default (0)

        Args:
            self

        Returns:
            None
        '''
        self.latitude = 0
        self.longitude = 0
        self.speed_limit = 0
        self.speed = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.warnings = 0
        self.violations = 0

    def set_api_key(self):
        '''
        Sets the HERE api key for the user
        
        Args:
            self

        Returns:
            None
        '''
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
        # Will replace the following line with self.speed_limit = reponse... once the request is correct
        self.speed_limit = 0
        return self.speed_limit
    
    def update_speed(self, new_speed):
        '''
        Updates the speed of the driver

        Args:
            self
            new_speed (float): The current speed

        Returns:
            None
        '''
        self.speed.append(new_speed)
        self.speed.pop(0)

    def get_speed(self):
        '''
        Returns the most recent speed

        Args:
            None

        Returns:
            self.speed (float): The most recent speed in the list
        '''
        return self.speed[-1]
    
    def get_prev_speed(self):
        '''
        Returns the previous speed

        Args:
            None

        Returns:
            self.speed (float): The previous speed in the list
        '''
        return self.speed[-2]

    def update_warnings(self):
        '''
        Updates the warnings amount based off of the data

        Args:
            self

        Returns:
            None
        '''
        if (self.speed_limit < self.speed[9]):
            self.warnings += 1

    def get_warnings(self):
        '''
        Returns the amount of warnings that a driver has

        Args:
            self
        
        Returns:
            self.warning (int): The number of warnings issued up to that point
        '''
        return int(self.warnings)
    
    def update_violations(self):
        '''
        Updates the amount of violations

        Args:
            self
            change (int): The amount to change the violations by

        Returns:
            None
        '''
        average = sum(self.speed) / len(self.speed)
        if (average > self.speed_limit):
            self.violations += 1
        
    def get_violations(self):
        '''
        Returns the amount of violations that a driver has

        Args:
            self
        
        Returns:
            self.violations (int): The number of violations issued up the that point
        '''
        return int(self.violations)