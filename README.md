# Driving_Stats
Gathers information about a person's driving habits and returns useful measures.

# Use Cases
* A parent who wants to monitor their teens driving.
    + Shows if they were speeding, how how long, and how far over the limit.
* Insurance companies that want to narrow down the cause of an accident
    + Shows if someone had enough time to react if both data sets are compared.
    + Shows if someone was brake checking based on the speed limit and deceleration.
* While not recommended, it could be used to legally race.
    + If two drivers start at the same place and have the same destination, they can have the app showing their speed relative to the speed limit.
    + For example, first person to get to the destination without getting any violations wins.
    + Compare 'race' times and stats against one another.
* Improving on driving skills.
    + If someone want's to see how they are driving compared to the average driver, they can review their stats.
    + They can do a side-by-side of similar trips.
    + For example seeing how work commutes change based off of time of day etc.
    + Show improvements over time by comparing driving summaries.

## Car Acceleration Averages
+ Sport 4.2
+ Coupe 5.4
+ Sedan 6.1
+ SUV 6.8
+ Truck 7.1
+ Wagon 7.2
+ Van 8.0
- https://hypertuned.com/guides/average-0-to-60#:~:text=According%20to%20our%20data%20of%20over%201%2C100%20different,60%20time%20for%20all%20cars%20is%206.1%20seconds.

The closer the acceleration is to 0, the more dangerous the driver is presummed to be. This would also depend on the vehicle type. Someone accelerating from 0-60 mph in 6.1 seconds in a sport is relatively slower than someone in a sedan. The sport would be holding back while the sedan would be flooring it. The vehicles are also meant to sustain the given acceleration associated with the type. A van with a sub 8.0 0-60 would be impressive but would not be sustainable UNLESS it has aftermarket modifications to assist. Additionally, someone who is constantly accelerating as much as possible would indicate unsafe driving behaviors. 

## Deceleration
All vehicle types should have an average deceleration that would be sustainable and safe. Deceleration would show the amount of time it would take for the car to slow down. Someone who is constantly slamming on the breaks would indicate unsafe driving behaviors. 

## Speed
This would be a simple indicator of how fast someone is going at any given time. Ideally, someone should be going the speed limit +-10mph. The exception would be on the freeway where the speed limit is the speed of traffic. The speed should be compared over multiple trips and multiple distances. This would allow for a better understanding of someones driving habbits. Someone going 15 over the speed limit over the course of a few seconds is considerably less dangerous than someone going 15 over the speed limit consitently. 

This is also used to calculate the average speed over or under the respecitve speed limit(s).
Ex. 
    Going between 3 different speed zones, 15mph, 30 mph, and 50mph. If the driver goes at 16mph, 32mph, and 33mph respectively, then the average speed limit difference would be +2mph. The larger the difference, the more dangerous a driver would be considered.

## Distance Traveled
The distance traveled would be used as supplimentary data used to calculate the average speed as well as the drivers habits. Someone driving reclessly over a short distance is not as severe as someone driving reclessly over a longer trip. Additionally, gas usage can be stored and predictions can be made based off of the users driving habits and the distance they plan to travel.


## AWS Database
The databse on the AWS server holder 2 main tables, one for the users and one for driving records. It also holds copies of the local trips data from the local database. 


## Local Database
The local database is a sqlite database that is used to store the most recent driving record before it is analyzed and sent to the aws database.
Storing it locally allows for the program to run even if there is no connection to the aws server. This database should be deleted after it is uploaded to the aws database to save space on the local device.


# Installs
All of the packages can be installed at once using the requirements.txt file.

To install all of the packages at once, use the following command:
pip install -r requirements.txt

More information on the packages is shown below:

HERE
pip install herepy

sql connector
pip install mysql-connector-python
https://realpython.com/python-mysql/

sqlite3
pip install sqlite3

# Keys
Here Api
https://platform.here.com/

AWS
https://aws.amazon.com/