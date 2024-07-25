#!/bin/env python3

'''
Gathers and uploads the driving data.
'''

import time, sys
from Stats.Support import Log
from Stats.Support.Driver import Driver
from Stats import LocalDB as ldb
from Stats import AwsDB as adb
from Stats import Analysis

__author__ = "Andy Hernandez"
__date__ = "7/9/2024"
__status__ = "Development"


LOGGER = Log.make_log()

def upload_to_aws(driver):
    '''
    Takes the data from the local database, analyzes it, and uploads it to the aws database.

    Args:
        None

    Returns:
        None
    '''
    LOGGER.info("Starting upload to AWS.")
    # Basic upload info
    time_span = "100"

    # Run analysis on data to get summed up info
    avg_speed = Analysis.average_speed()
    avg_acc = Analysis.avg_acceleration()
    avg_dec = Analysis.avg_deceleration()
    max_speed = Analysis.max_speed()
    max_acc = Analysis.max_acceleration()
    min_dec = Analysis.min_deceleration()

    # Format
    data = adb.format(
        driver, 
        time_span, 
        max_speed, 
        avg_speed, 
        max_acc, 
        avg_acc, 
        min_dec, 
        avg_dec
    )

    # Upload to aws
    con = adb.connect_aws_db()
    adb.upload(con, data)
    LOGGER.info("Upload to AWS complete.")

def run(driver):
    '''
    Gets the data from a device and updates the local database

    Args:
        driver (Driver): The current person driving and their information.

    Returns:
        None
    '''
    LOGGER.info(f"Gathering data for driver {driver.name}")
    # Getting the starting parameters 
    longitude, latitude = driver.update_location()
    print(longitude, latitude)
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
        acceleration = ldb.set_acceleration(driver, interval)
        longitude, latitude = driver.get_location()
        data = ldb.format(latitude, longitude, 0, speed, acceleration)
        # data = ldb.format(latitude, longitude, driver.get_speed_limit(), speed, acceleration)
        ldb.upload(data)
        time.sleep(interval)
    LOGGER.info("Finished gathering data from the driver.")


def main():
    '''
    The runs the data gathering and uploads the data to aws

    Args:
        None

    Returns:
        None
    '''
    LOGGER.info("Starting data collection")
    
    # Creating driver
    driver = "John Smith"
    license = "Y123456"
    driver = Driver(driver, 30, "Male", license, "SUV")
    driver.set_api_key()
    ldb.delete()
    ldb.create_database()
    run(driver)
    upload_to_aws(driver)

    # try:
        # ldb.create_database()
        # run(driver)
        # upload_to_aws(driver)
        # ldb.print_all()
        # ldb.delete()
    # except Exception as e:
        # LOGGER.error(f"Error occured during main upload: {e}")
        # sys.exit(f"Error occured during main upload: {e}")

if (__name__ == "__main__"):
    main()