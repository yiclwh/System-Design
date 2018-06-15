"""
Support two basic uber features:

Drivers report their locations.
Rider request a uber, return a matched driver.
When rider request a uber, match a closest available driver with him, then mark the driver not available.

When next time this matched driver report his location, return with the rider's information.

You can implement it with the following instructions:

report(driver_id, lat, lng)
1) return null if no matched rider.
2) return matched trip information.

request(rider_id, lat, lng)
1) create a trip with rider's information.
2) find a closest driver, mark this driver not available.
3) fill driver_id into this trip.
4) return trip

This is the definition of Trip in Java:

public class Trip {
    public int id; // trip's id, primary key
    public int driver_id, rider_id; // foreign key
    public double lat, lng; // pick up location
}

Example
report(1, 36.1344, 77.5672) // return null
report(2, 45.1344, 76.5672) // return null
request(2, 39.1344, 76.5672) // return a trip, LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
report(1, 38.1344, 75.5672) // return a trip, LOG(INFO): Trip(rider_id: 2, driver_id: 1, lat: 39.1344, lng: 76.5672)
report(2, 45.1344, 76.5672) // return null
"""

'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper

class Location:
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

class MiniUber:

    def __init__(self):
        # initialize your data structure here.
        self.driver2Location = {}
        self.driver2Trip = {}

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        # Write your code here
        if driver_id in self.driver2Trip:
            return self.driver2Trip[driver_id]

        if driver_id in self.driver2Location:
            self.driver2Location[driver_id].lat = lat
            self.driver2Location[driver_id].lng = lng
        else:
            self.driver2Location[driver_id] = Location(lat, lng)

        return None

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        # Write your code here
        trip = Trip(rider_id, lat, lng)
        distance, driver_id = -1, -1

        for key, value in self.driver2Location.items():
            dis = Helper.get_distance(value.lat, value.lng, lat, lng);
            if distance < 0 or distance > dis:
                driver_id = key
                distance = dis

        if driver_id != -1:
            del self.driver2Location[driver_id]

        trip.driver_id = driver_id;
        self.driver2Trip[driver_id] = trip

        return trip