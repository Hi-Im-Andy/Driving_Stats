#!/bin/env python3

'''
Used to create a log file and keep track of actions taken while running.
'''

import os
import logging
from logging.handlers import RotatingFileHandler

__author__ = "Andy Hernandez"
__date__ = "07/1/2024"
__status__ = "Development"

def make_log():
    '''
    Creates a log file and sets up logging for the program.
    
    Args:
        None
    
    Returns:
        logger (var): The variable that holds the logging information
    '''
    # Setting up the logger path and name
    log_name = "driver_app"
    logger = logging.getLogger(log_name) 
    path = os.path.dirname(__file__)
    log_file_name = os.path.join(path, f"{log_name}.log")

    # Setting up the logger
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt = "%(asctime)s: %(levelname)-8s %(message)s", datefmt = "%d/%m/%Y %H:%M:%S"
    )

    file_handler = RotatingFileHandler(
        filename = log_file_name,
        mode = 'a',
        maxBytes = 1024*1024,
        backupCount = 1,
        encoding = None,
        delay = 0
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Adding a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def test_logger():
    logger = make_log()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

if (__name__ == "__main__"):
    test_logger()