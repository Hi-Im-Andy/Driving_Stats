#!/bin/env

'''Used for the creation and manipulation of the local database.'''

import sqlite3
from datetime import datetime
import math

__author__ = "Andy Hernandez"
__date__ = "07/02/2024"
__status__ = "Development"

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
        decceleration FLOAT
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


# Should only take in the acceleration, then output a single number based on acc or dec
def format(latitude, longitude, limit, speed, acceleration, decceleration):
    '''
    Formats the data into a list that can be used in a query

    Args:
        latitude (float): The latitude of the current position.
        longitude (float): The longitude of the current position.
        limit (int): The speed limit of the current location.
        speed (float): The current speed of the vehicle.
        acceleration (float): The current acceleration of the vehicle.
        decceleration (float): The current decceleration of the vehicle.
    
    Returns:
        data (list): The ordered arguments along with the current time.
    '''
    date_format = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    data = [date_format, latitude, longitude, speed, limit, acceleration, decceleration]
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

def set_speed(latitude, longitude, interval):
    '''
    Calculates the current speed based off of the distance traveled over an interval

    Args:
        latitude (float): The latitude of the current position
        longitude (float): The longitude of the current position
        interval (int): The interval in seconds
    
    Returns:
        speed (float): The speed in miles per hour
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT latitude, longitude FROM trip ORDER BY time DESC LIMIT 1")
    last = c.fetchone()
    conn.close()
    lat1, lon1 = last
    distance = math.sqrt(((latitude-lat1)**2) + ((longitude-lon1)**2))
    speed = float(distance / interval)
    return speed

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

def get_decceleration():
    '''
    Gets the deccelerations from the entire trip

    Args:
        None

    Returns:
        c.fetchall() (list): A list of all of the deccelerations during the trip
    '''
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT decceleration FROM trip")
    return c.fetchall()


if (__name__ == "__main__"):
    # create_database()
    # i = 0
    # while (i < 100):
    #     data = format(1, 2, 3, 4, 5, 6)
    #     upload(data)
    #     time.sleep(1)
    #     i += 1
    # speed = get_speed()
    # speed = [value[0] for value in speed]
    # print(max(speed))
    # print((sum(speed))/len(speed))
    set_speed(2,4,1)