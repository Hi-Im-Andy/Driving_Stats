# Simulates the device that would be uploading the data (phone or on board device in the vehicle)
import time, sys, random
from Stats.Support import Log, Driver
from Stats import LocalDB as ldb
from Stats import AwsDB as adb
from Stats import Analysis


def upload_to_aws():
    '''
    Takes the data from the local database, analyzes it, and uploads it to the aws database.

    Args:
        None

    Returns:
        None
    '''
    # Basic upload info
    driver = "John Smith"
    license = "Y123456"
    time_span = "100"
    new_driver = Driver(driver, 30, "Male", license, "SUV")

    # Run analysis on data to get summed up info
    avg_speed = Analysis.average_speed()
    avg_acc = Analysis.avg_acceleration()
    avg_dec = Analysis.avg_decceleration()
    max_speed = Analysis.max_speed()
    max_acc = Analysis.max_acceleration()
    min_dec = Analysis.min_decceleration()
    
    warnings = Analysis.warnings()
    violations = Analysis.violations()

    # Format
    data = adb.format(
        new_driver, 
        time_span, 
        max_speed, 
        avg_speed, 
        max_acc, 
        avg_acc, 
        min_dec, 
        avg_dec, 
        warnings, 
        violations
    )

    # Upload to aws
    adb.upload(data)

def sample_run():
    '''
    Simulates a straight drive with changes in speed and updates the local database

    Args:
        None

    Returns:
        None
    '''
    time_start = time.time()

    longitude = 0
    latitude = 0

    out = ldb.format(0, 0, 0, 0, 0)
    ldb.upload(out)
    time.sleep(1)
    
    while(time.time() - time_start < 60):
        longitude += (0.00001 * random.randrange(9)) 
        latitude += 0.00001
        speed = ldb.set_speed(latitude, longitude, 1)
        acceleration = ldb.set_acceleration(speed, 1)
        out = ldb.format(latitude, longitude, 0, speed, acceleration)
        ldb.upload(out)
        time.sleep(1)

def main():
    '''
    The runs the data gathering and uploads the data to aws

    Args:
        None

    Returns:
        None
    '''
    logger = Log.make_log()
    logger.info("Starting data collection")
    try:
        ldb.create_database()
        sample_run()
        # upload_to_aws
        ldb.print_all()
        ldb.delete()
    except Exception as e:
        logger.error(f"Error occured during main upload: {e}")
        sys.exit(f"Error occured during main upload: {e}")

if (__name__ == "__main__"):
    main()
