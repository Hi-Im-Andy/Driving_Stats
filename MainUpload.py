#!/bin/env python3

'''
Gathers and uploads the driving data.
'''

import time, sys, random
from Stats.Support import Log
from Stats.Support.Driver import Driver
from Stats import LocalDB as ldb
from Stats import AwsDB as adb
from Stats import Analysis

__author__ = "Andy Hernandez"
__date__ = "7/9/2024"
__status__ = "Development"


def upload_to_aws(driver):
    '''
    Takes the data from the local database, analyzes it, and uploads it to the aws database.

    Args:
        None

    Returns:
        None
    '''
    # Basic upload info
    time_span = "100"

    # Run analysis on data to get summed up info
    avg_speed = Analysis.average_speed()
    avg_acc = Analysis.avg_acceleration()
    avg_dec = Analysis.avg_decceleration()
    max_speed = Analysis.max_speed()
    max_acc = Analysis.max_acceleration()
    min_dec = Analysis.min_decceleration()
    
    warnings = Analysis.warnings()
    violations = Analysis.violations()

    # Format
    data = adb.format(
        driver, 
        time_span, 
        max_speed, 
        avg_speed, 
        max_acc, 
        avg_acc, 
        min_dec, 
        avg_dec, 
        warnings, 
        violations
    )

    # Upload to aws
    adb.upload(data)

def sample_run():
    '''
    Simulates a straight drive with changes in speed and updates the local database

    Args:
        None

    Returns:
        None
    '''
    time_start = time.time()

    longitude = 0
    latitude = 0

    out = ldb.format(0, 0, 0, 0, 0)
    ldb.upload(out)
    time.sleep(1)
    
    while(time.time() - time_start < 60):
        longitude += (0.00001 * random.randrange(9)) 
        latitude += 0.00001
        speed = ldb.set_speed_sample(latitude, longitude, 1)
        acceleration = ldb.set_acceleration(speed, 1)
        out = ldb.format(latitude, longitude, 0, speed, acceleration)
        ldb.upload(out)
        time.sleep(1)

def run(driver):
    '''
    Gets the data from a device and updates the local database

    Args:
        driver (Driver): The current person driving and their information.

    Returns:
        None
    '''
    # Getting the starting parameters 
    longitude, latitude = driver.update_location()
    out = ldb.format(longitude, latitude, 0, 0, 0)
    ldb.upload(out)
    interval = 1
    time.sleep(interval)

    # The True conditional needs to be linked to something like a button press if a UI is made
    # Updates the database with new entries in 1 second intervals
    # while(True):
    i = 0
    while (i <= 60):
        i += 1
        speed = ldb.set_speed(driver, 1)
        acceleration = ldb.set_acceleration(speed, interval)
        longitude, latitude = driver.get_location()
        data = ldb.format(latitude, longitude, driver.get_speed_limit(), speed, acceleration)
        ldb.upload(data)
        time.sleep(interval)


def main():
    '''
    The runs the data gathering and uploads the data to aws

    Args:
        None

    Returns:
        None
    '''
    logger = Log.make_log()
    logger.info("Starting data collection")
    
    # Creating driver
    driver = "John Smith"
    license = "Y123456"
    driver = Driver(driver, 30, "Male", license, "SUV")
    driver.set_api_key()
    
    try:
        ldb.create_database()
        # sample_run()
        run(driver)
        # upload_to_aws(driver)
        ldb.print_all()
        ldb.delete()
    except Exception as e:
        logger.error(f"Error occured during main upload: {e}")
        sys.exit(f"Error occured during main upload: {e}")

if (__name__ == "__main__"):
    main()
