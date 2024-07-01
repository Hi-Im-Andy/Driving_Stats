#!/bin/env python3

'''
Used to get metrics from the data (average speed, max acceleration, etc).
'''

import GetData
import Visuals

__author__ = "Andy Hernandez"
__date__ = "6/30/2024"

def average_speed(user_id):
    query = '''
    GET * FROM Speed WHERE User_ID = ?
    '''
    all_speed = print() # Place holders while I commit.
    data = GetData.get_data(query, user_id)