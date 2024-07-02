#!/bin/env python3

'''Gets the data from the AWS SQL database.'''

from mysql.connector import connect, Error
from getpass import getpass

__author__ = "Andy Hernandez"
__data__ = "06-30-2024"
__status__ = "Development"


############################################################
# All User Trips
############################################################
# All user trips should be stored on the aws mysql database
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
    CREATE TABLE users (
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

    create_driving_record = """
    CREATE TABLE driving_record (
        id INT AUTO_INCREMENT PRIMARY KEY,
        date DATE,
        time TIME,
        
    )
    """

def acceleration_comparison(car_type, acc_time):
    '''
    Compares the input car type and average acceleration and returns the delta from average.
    
    Args:
        car_type (str): The car type determines what time should be compared
        acc_time (float): Given acceleration for the trip that will be compared to the overall average

    Returns:
        acc_delta (float): Acceleration difference for the given vehicle type and the given acceleration
    '''
    




if (__name__ == "__main__"):
    try:
        create_aws_db()
        #connect_aws_db()
    except Error as e:
        print(e)
