# Simulates the device that would be uploading the data (phone or on board device in the vehicle)
import time
import random
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
        driver, 
        license, 
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

    # upload to aws
    adb.upload(data)

def sample_run():
    time_start = time.time()

    longitude = 0
    latitude = 0

    out = ldb.format(0, 0, 0, 0, 0)
    ldb.upload(out)
    time.sleep(1)
    
    # Simulating a striaght drive with variable change in position/speed/acceleration 
    while(time.time() - time_start < 60):
        longitude += (0.00001 * random.randrange(9)) 
        latitude += 0.00001
        speed = ldb.set_speed(latitude, longitude, 1)
        acceleration = ldb.set_acceleration(speed, 1)
        out = ldb.format(latitude, longitude, 0, speed, acceleration)
        ldb.upload(out)
        time.sleep(1)

def main():
    ldb.create_database()
    sample_run()

    # upload_to_aws
    ldb.print_all()
    # ldb.delete()
        
        

if (__name__ == "__main__"):
    main()
