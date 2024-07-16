#!/bin/env

'''Used for the creation and manipulation of the local database.'''

import sqlite3
from datetime import datetime
import math

__author__ = "Andy Hernandez"
__date__ = "07/02/2024"
__status__ = "Development"


##############################################################
# Create, delete, and other basic functions
##############################################################
def create_database():
    '''
    Creates the database and tables for the program to use
    
    Args:
        None

    Returns:
        None
    '''
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS trip (
        time PRIMARY KEY,
        latitude FLOAT,
        longitude FLOAT,
        speed FLOAT,
        speed_limit INT,
        acceleration FLOAT,
        deceleration FLOAT
    )
    ''')

def delete():
    '''
    Drops the table from the database

    Args:
        None

    Returns:
        None
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DROP TABLE trip")

def clear():
    '''
    Removes all data inside of the table

    Args:
        None

    Returns: 
        None
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("TRUNCATE TABLE IF EXISTS trip")

def format(latitude, longitude, limit, speed, acceleration):
    '''
    Formats the data into a list that can be used in a query

    Args:
        latitude (float): The latitude of the current position.
        longitude (float): The longitude of the current position.
        limit (int): The speed limit of the current location.
        speed (float): The current speed of the vehicle.
        acceleration (float): The current acceleration of the vehicle.
        deceleration (float): The current deceleration of the vehicle.
    
    Returns:
        data (list): The ordered arguments along with the current time.
    '''
    if (acceleration < 0):
        deceleration = acceleration
        acceleration = 0
    else:
        deceleration = 0
        
    # Setting the date and time in the event of a driver rolling over to the following day
    date_format = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    data = [date_format, latitude, longitude, speed, limit, acceleration, deceleration]
    return data

def upload(data):
    '''
    Uploads the data to the database
    
    Args:
        data (list): A list of the individual inputs for the database

    Returns:
        None
    '''
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO trip VALUES (?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

def get_all():
    '''
    Gets all the data from the database
    
    Args:
        None

    Returns:
        c.fetchall() (List): The list that holds all of the rows and columns of the database 
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM trip")
    return c.fetchall()

def print_all():
    '''
    Prints all of the elements in the database as a list

    Args:
        None

    Returns:
        None
    '''
    data = get_all()
    for row in data:
        print(row)


##############################################################
# Speed and acceleration
##############################################################
def set_speed(driver, interval):
    '''
    Calculates the current speed based off of the distance traveled over an interval

    Args:
        driver (Driver): The driver that is currently driving and their information
        interval (int): The interval in seconds
    
    Returns:
        speed (float): The speed in miles per hour
    '''
    # Getting the last location, updating, then getting the current location
    lat1, lon1 = driver.get_location()
    longitude, latitude = driver.update_location()
    # Converting the location difference into distance over time then converting to mph
    lat1, lon1, latitude, longitude = math.radians(lat1), math.radians(lon1), math.radians(latitude), math.radians(longitude)
    distance = 6371 * math.sqrt(((latitude-lat1)**2) + ((longitude-lon1)**2))
    speed = float(distance / interval * 3600)
    speed = speed * 0.911344416 * 0.68181818
    # Updating and returning the most recent speed
    driver.update_speed(speed)
    return speed

def set_acceleration(driver, interval):
    '''
    Calculates the current acceleration or deceleration based off of the change of speed in the last interval

    Args:
        speed (float): The speed in miles per hour of the current input
        interval(int): The interval in seconds

    Returns:
        acceleration (flaot): The change in speed in miles per hour per second
    '''
    acceleration = (driver.get_speed() - driver.get_prev_speed()) / interval
    return acceleration

def get_speed():
    '''
    Gets all of the speeds during the trip

    Args:
        None

    Returns:
        c.fetchall() (list): A list of all of the speeds during the trip
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT speed FROM trip")
    return c.fetchall()

def get_acceleration():
    '''
    Gets the accelerations from the entire trip

    Args:
        None
    
    Returns:
        c.fetchall() (list): A list of all of the accelerations during the trip
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT acceleration FROM trip")
    return c.fetchall()

def get_deceleration():
    '''
    Gets the decelerations from the entire trip

    Args:
        None

    Returns:
        c.fetchall() (list): A list of all of the decelerations during the trip
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT deceleration FROM trip")
    return c.fetchall()


if (__name__ == "__main__"):
    set_speed(2,4,1)