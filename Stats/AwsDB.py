#!/bin/env python3

'''Gets the data from the AWS SQL database.'''

from mysql.connector import connect, Error
from getpass import getpass
from datetime import datetime
import LocalDB as ldb

__author__ = "Andy Hernandez"
__data__ = "06-30-2024"
__status__ = "Development"


##############################################################
# Connection and creation of AWS table
##############################################################
def create_aws_db():
    '''
    Creates a new database in the aws server for the driving stats

    Args:
        None

    Returns:
        None
    '''
    with connect(
        host = input("Host: "),
        user = input("User: "),
        password = getpass("Password: ")
    ) as connection:
        create_query = "CREATE DATABASE IF NOT EXISTS driverdb"
        with connection.cursor() as cursor:
            cursor.execute(create_query)

def connect_aws_db():
    '''
    Connects to the aws driving stats database

    Args:
        None

    Returns:
        Connection (var): The sql connection to the database
    '''
    with connect(
        host = input("Host: "),
        user = input("User: "),
        password = getpass("Password: "),
        database = "driverdbs"
    ) as connection:
        print(connection)
        return connection
    
def create_driving_table():
    '''
    Creates a new table for the driving records for an aws database

    Args:
        None

    Returns:
        None
    '''
    connection = connect_aws_db()
    create_driving_record = '''
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
        Min_deceleration Float,
        average_deceleration FLOAT,
        warnings INT,
        violations INT,
        trip VARCHAR(100)
    )
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_driving_record)
        connection.commit()
        connection.close()


##############################################################
# Uploads
##############################################################
def format(driver, time_span, max_speed, avg_speed, max_acc, avg_acc, min_dec):
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
    
    Returns:
        data (list): The list of the ordered inputs
    '''
    # trip = f"{driver.license}{datetime.now().strftime("%m%d$Y%H%M%S")}"
    date = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    trip = f"test{date}"
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
        driver.warnings,
        driver.violations,
        trip
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
        cursor.execute("INSERT INTO driving_record (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
        connection.commit()
        connection.close()


##############################################################
# Users table
##############################################################
def create_user_table():
    '''
    Creates a new table for the user(s) in the aws database
    
    Args:
        None

    Returns:
        None
    '''
    connection = connect_aws_db()
    create_users_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT,
        gender VARCHAR(100),
        license VARCHAR(100) NOT NULL,
        car_type VARCHAR(100) NOT NULL
    )
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_users_query)
        connection.commit()
        connection.close()

##############################################################
# Trip Tables
##############################################################
def create_trip(trip_name):
    '''
    Creates a new table in the aws database with all of the information from the local database
    
    Args:
        trip_name (str): The name that is used to reference the table

    Returns:
        None
    '''
    connection = connect_aws_db()
    with connection.cursor() as cursor:
        query = f'''
            INSERT INTO {trip_name}
            SELECT * FROM [database].[trip]
        '''
        cursor.execute(query)

def query_trip(trip_query):
    '''
    Returns list from the specified query

    Args:
        trip_query (str): The query that should be used (query and table should be included)
    
    Returns:
        cursor.fetchall() (list): A list with the output from the query
    '''
    connection = connect_aws_db()
    with connection.cursor() as cursor:
        cursor.execute(trip_query)
        return cursor.fetchall()


##############################################################
# Table Removal
##############################################################
def delete():
    '''
    Drops all tables from the database

    Args:
        None

    Returns:
        None
    '''
    connection = connect_aws_db()
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS driving_record")
        cursor.execute("DROP TABLE IF EXISTS users")

def full_delete():
    connection = connect_aws_db()
    with connection.cursor() as cursor:
        cursor.execute("SELECT trip from driving_record")
        trips = cursor.fetchall()
        for trip in trips:
            cursor.execute("DROP TABLE IF EXISTS %s", (trip[0],))
    delete()

def clear():
    '''
    Clears all of the data inside of the tables

    Args:
        None

    Returns:
        None
    '''
    connection = connect_aws_db()
    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE IF EXISTS driving_record")
        cursor.execute("TRUNCATE TABLE IF EXISTS users")


if (__name__ == "__main__"):
    try:
        # create_aws_db()
        connect_aws_db()
    except Error as e:
        print(e)