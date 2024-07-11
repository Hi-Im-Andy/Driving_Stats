#!/bin/env python3

'''Gets the data from the AWS SQL database.'''

from mysql.connector import connect, Error
from getpass import getpass
from datetime import datetime

__author__ = "Andy Hernandez"
__data__ = "06-30-2024"
__status__ = "Development"


##############################################################
# Connection and creation of AWS table
##############################################################
def create_aws_db():
    with connect(
        host = input("Host: "),
        user = input("User: "),
        password = getpass("Password: "),
    ) as connection:
        create_query = "CREATE DATABASE driving_stats"
        with connection.cursor() as cursor:
            cursor.execute(create_query)


def connect_aws_db():
    with connect(
        host = input("Host: "),
        user = input("User: "),
        password = getpass("Password: "),
        database = "driving_stats",
    ) as connection:
        print(connection)
        return connection

def create_tables():
    connection = connect_aws_db()
    create_users_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        gender VARCHAR(100),
        license VARCHAR(100) NOT NULL,
        car_type VARCHAR(100) NOT NULL
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_users_query)
        connection.commit()
    # 
    create_driving_record = """
    CREATE TABLE IF NOT EXISTS driving_record (
        id INT AUTO_INCREMENT PRIMARY KEY,
        driver VARCHAR(100),
        license VARCHAR(100),
        date DATE,
        time_span TIME,
        max_speed FLOAT,
        average_speed FLOAT,
        max_acceleration FLOAT,
        average_acceleration FLOAT,
        Min_decceleration Float,
        average_decceleration FLOAT,
        warnings INT,
        violations INT
    )
    """ 
    with connection.cursor() as cursor:
        cursor.execute(create_driving_record)
        connection.commit()
        connection.close()

##############################################################
# Uploads
##############################################################
def format(driver, time_span, max_speed, avg_speed, max_acc, avg_acc, min_dec, warnings, violations):
    '''
    Places all of the input arguments into a list to prepare them for the query

    Args:
        driver (class): The class with the drivers information
        time_span (str): The time span of the trip
        max_speed (float): The maximum speed of the trip
        avg_speed (float): The average speed of the trip
        max_acc (float): The maximum acceleration of the trip
        avg_acc (float): The average acceleration of the trip
        min_dec (float): The minimum deceleration of the trip
        warnings (int): The number of warnings the driver received during the trip
        violations (int): The number of violations the driver received during the trip
    
    Returns:
        data (list): The list of the ordered inputs
    '''
    date = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    data = [
        driver.name, 
        driver.license,
        date, 
        time_span, 
        max_speed, 
        avg_speed, 
        max_acc,
        avg_acc,
        min_dec,
        warnings,
        violations
    ]
    return data

def upload(data):
    '''
    Uploads the analyzed trip data to the aws database

    Args:
        data (list): The formatted inputs for the insert query

    Returns:
        None
    '''
    connection = connect_aws_db()
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO driving_record (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        connection.commit()
        connection.close()

# Should add the option to upload the trip data from the local db


##############################################################
# Users Database
##############################################################

# Use existing user management systems?
# Post the device ID
# Return the user info
# Adding the user to the DB based on the device.
# Post multiple devices to the same user if wanted.
# Change user
# Delete user
# Delete user from DB
# Delete device from user
# Get user
# Get user devices
# Change user


if (__name__ == "__main__"):
    try:
        create_aws_db()
        #connect_aws_db()
    except Error as e:
        print(e)


