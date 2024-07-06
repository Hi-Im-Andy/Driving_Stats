#!/bin/env

'''Used for the creation and manipulation of the local database.'''

import sqlite3
from datetime import datetime
import math

__author__ = "Andy Hernandez"
__date__ = "07/02/2024"
__status__ = "Development"

def create_database():
    '''Creates the database and tables for the program to use.'''
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

def format(latitude, longitude, limit, speed, acceleration, decceleration):
    '''Formats the data for the database.'''
    date_format = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    data = [date_format, latitude, longitude, speed, limit, acceleration, decceleration]
    return data

def upload(data):
    '''Uploads the data to the database.'''
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO trip VALUES (?, ?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

def get_all():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM trip")
    return c.fetchall()

def set_speed(latitude, longitude, interval):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT latitude, longitude FROM trip ORDER BY time DESC LIMIT 1")
    last = c.fetchone()
    conn.close()
    lat1, lon1 = last
    distance = math.sqrt(((latitude-lat1)**2) + ((longitude-lon1)**2))
    speed = float(distance / interval)
    print(speed)
    return speed


def get_speed():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT speed FROM trip")
    return c.fetchall()

def delete_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("DROP TABLE trip")


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