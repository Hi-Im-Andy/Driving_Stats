#!/bin/env python3

'''Gets the data from the AWS SQL database.'''

from mysql.connector import connect, Error
from getpass import getpass
from datetime import datetime
import LocalDB as ldb

__author__ = "Andy Hernandez"
__data__ = "06-30-2024"
__status__ = "Development"

# This entire file can be turned into a class similar to Driver.
# However, this will be kept as is to show versitility without the use of classes.

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
        # This can also be created in aws manually without needing to query.
        create_query = "CREATE DATABASE IF NOT EXISTS driverdb"
        with connection.cursor() as cursor:
            cursor.execute(create_query)

def connect_aws_db():
    '''
    Gets the information for the aws database from the user and returns it

    Args:
        None

    Returns:
        connect_dict (dict): A dictionary with the host, user, password, and database that is used to connect to the database 
    '''
    host = input("Host: ")
    user = input("User: ")
    password = getpass("Password: ")
    database = "driverdb"
    connect_dict = {"Host" : host, "User" : user, "Password" : password, "Database" : database}
    return connect_dict
    
def create_driving_table(con):
    '''
    Creates a new table for the driving records for an aws database

    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database

    Returns:
        None
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
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

def upload(con, data):
    '''
    Uploads the analyzed trip data to the aws database

    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database
        data (list): The formatted inputs for the insert query

    Returns:
        None
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO driving_record (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
            connection.commit()
            connection.close()


##############################################################
# Users table
##############################################################
def create_user_table(con):
    '''
    Creates a new table for the user(s) in the aws database
    
    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database

    Returns:
        None
    '''
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
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_users_query)
            connection.commit()
            connection.close()

##############################################################
# Trip Tables
##############################################################
def create_trip(con, trip_name):
    '''
    Creates a new table in the aws database with all of the information from the local database
    
    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database
        trip_name (str): The name that is used to reference the table

    Returns:
        None
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        with connection.cursor() as cursor:
            query = f'''
                INSERT INTO {trip_name}
                SELECT * FROM [database].[trip]
            '''
            cursor.execute(query)
            connection.commit()
            connection.close()

def query_trip(con, trip_query):
    '''
    Returns list from the specified query

    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database
        trip_query (str): The query that should be used (query and table should be included)
    
    Returns:
        cursor.fetchall() (list): A list with the output from the query
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(trip_query)
            return cursor.fetchall()


##############################################################
# Table Removal
##############################################################
def delete(con):
    '''
    Drops only the driving_record and users tables from the database

    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database

    Returns:
        None
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS driving_record")
            cursor.execute("DROP TABLE IF EXISTS users")

def full_delete(con):
    '''
    Drops all of the tables from the database

    Args:
       con (dict): A dictionary with the host, user, password, and database that is used to connect to the database
    
    Returns:
        None
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT trip from driving_record")
            trips = cursor.fetchall()
            for trip in trips:
                cursor.execute("DROP TABLE IF EXISTS %s", (trip[0],))
    delete(con)

def clear(con):
    '''
    Clears all of the data inside of the tables

    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database

    Returns:
        None
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE IF EXISTS driving_record")
            cursor.execute("TRUNCATE TABLE IF EXISTS users")
            
def show(con):
    '''
    Shows all of the tables in the database

    Args:
        con (dict): A dictionary with the host, user, password, and database that is used to connect to the database

    Returns:
        None
    '''
    with connect(
        host = con["Host"],
        user = con["User"],
        password = con["Password"],
        database = con["Database"]
    ) as connection:
        query = "SHOW TABLES"
        with connection.cursor() as cursor:
            cursor.execute(query)
            print(cursor.fetchall())
            connection.commit()
            connection.close()


if (__name__ == "__main__"):
    try:
        con = connect_aws_db()
        # create_aws_db(con)
        # connect_aws_db(con)
        # create_driving_table(con)
        show(con)
    except Error as e:
        print(e)