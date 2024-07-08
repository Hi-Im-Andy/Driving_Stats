# Simulates the device that would be uploading the data (phone or on board device in the vehicle)
import time
import random
from Stats import LocalDB as ldb
from Stats import AwsDB as adb

def upload_to_aws(trip_data):
    # Get average acceleration
    # Get max acceleration
    # Get min acceleration
    # Get average speed
    # Get max speed

    # Format

    # upload to aws

    print()

def sample_run():
    time_start = time.time()

    longitude = 0
    latitude = 0

    out = ldb.format(0, 0, 0, 0, 0, 0)
    ldb.upload(out)
    time.sleep(1)
    while(time.time() - time_start < 60):

        # Simulating a striaght drive with variable change in position/speed/acceleration 
        longitude += (0.00001 * random.randrange(9)) 
        latitude += 0.00001
        speed = ldb.set_speed(latitude, longitude, 1)
        out = ldb.format(latitude, longitude, 0, speed, 0, 0)
        ldb.upload(out)
        time.sleep(1)

def main():
    ldb.create_database()
    sample_run()

    # upload_to_aws
    ldb.print_all()
    ldb.delete()
        
        

if (__name__ == "__main__"):
    main()
