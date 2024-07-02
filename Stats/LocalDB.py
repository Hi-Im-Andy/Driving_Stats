#!/bin/env

'''Used for the creation and manipulation of the local database.'''

import sqlite3
import os, sys, time

__author__ = "Andy Hernandez"
__date__ = "07/02/2024"
__status__ = "Development"

def create_database():
    '''Creates the database and tables for the program to use.'''
    conn = sqlite3.connect('database.db')
    #...

def connect_database():
    #...
    return sqlite3.connect('database.db')

if (__name__ == "__main__"):
    create_database()