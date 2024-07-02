#!/bin/env python3

'''Outputs the useful data gathered by the on board device.'''

import os
from Stats import Visuals, LocalDB, AwsDB
from Stats.Support import Log, Driver

def add_driver():
    '''
    Adds the driver to the system.

    Args:
        None
    Returns:
        None
    '''
    name = "John Smith"
    age = 30
    gender = "Male"
    lic = "Y12345678"
    car_type = "Truck"
    



if(__name__ == "__main__"):
    logger = Log.make_log()
    current_driver = Driver("John Smith", )
    logger.info(f"Main is running.")
    AwsDB.get_all()