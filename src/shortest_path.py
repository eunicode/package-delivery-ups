import csv
import datetime
import math

from helper import print_csv
from helper import str_to_timedelta

# Copy "distances" csv data
# Space complexity = O(N)
# Time complexity = O(N)
# Open csv file as a text file and get a file object
with open("csv/distance_data.csv") as csv_file:
    # Convert file object to iterable reader object
    csv_reader_dist = csv.reader(csv_file, delimiter=",")

    # Convert reader object to list
    csv_reader_dist = list(csv_reader_dist)  # 2D list [ ["0.0", "", "", ""], ....]
    # print(csv_reader_dist)
    # print_csv(csv_reader_dist)

# Copy location csv data
# Space complexity = O(N)
# Time complexity = O(N)
with open("csv/location_data.csv") as csv_file_location:
    csv_reader_location = csv.reader(csv_file_location, delimiter=",")
    csv_reader_location = list(csv_reader_location)

    # ------------------------------------------------------------------
    # Calculate current total traveled distance
    # Add distance to a distance accumulator variable passed in as an argument
    # Time complexity = O(1)
    def distance_accumulate(row_value, column_value, dist_acc):
        # Distance btw loc #1 and loc #2
        distance = csv_reader_dist[row_value][column_value]

        if (
            distance == ""
        ):  # If distance btw loc #2 to loc #1 is empty string, reverse. The dist btw A & B is the same as B & A.
            distance = csv_reader_dist[column_value][row_value]

        # Add distance to distance accumulator
        dist_acc += float(distance)
        return dist_acc

    # ------------------------------------------------------------------
    # Find the distance between location #1 and location #2
    # Time complexity = O(1)
    def distance_get(row_value, column_value):
        # Distance btw loc #1 and loc #2
        distance = csv_reader_dist[row_value][column_value]

        # Distance btw loc #2 and loc #1
        if distance == "":
            distance = csv_reader_dist[column_value][row_value]

        return float(distance)

    # ------------------------------------------------------------------
    # Calculate accumulated time. Also calculate and store time intervals.
    # Time complexity = O(N)
    def time_accumulate(dist, time):
        # Calculate the time it took to travel a distance by using the truck's speed (18 mph).
        hours = dist / 18  # miles * (1 hour/18 miles) = hours
        # Take hours float and format it into a string of hours and minutes
        minutes = "{0:02.0f}:{1:02.0f}".format(*divmod(hours * 60, 60))
        time_string = minutes + ":00"  # Add seconds to string

        # Add time interval to `time` list
        time.append(time_string)  # `time` is parameter

        total_time = datetime.timedelta()
        # Add all the time intervals in `time` list
        for t in time:
            d = str_to_timedelta(t)  # Convert string to timedelta
            total_time += d

        return total_time

    # ------------------------------------------------------------------
    # Lists to hold packages in the optimized order
    truck1_pkg_seq = []
    truck1_loc_seq = []
    truck2_pkg_seq = []
    truck2_loc_seq = []
    truck3_pkg_seq = []
    truck3_loc_seq = []

    # Find a sequence of packages to deliver that will minimize the travel distance.
    # This is a single source shortest path algorithm that uses a greedy approach.
    # The algorithm uses lists to store visited locations and unvisited locations.
    # The algorithm works by searching for the closest location to its current location.
    # Once it finds the closest location, it adds that location to the visited-locations list, and
    # removes that location from locations-to-visit list.
    # The time complexity is O(N^2) because it has a while loop with a nested for loop.
    # The while loop keeps running until the locations-to-visit list is empty.
    # The inner for loop iterates the locations-to-visit list until it finds the closest location.
    # Once the for loop finds the closest location, it updates the current location and removes that
    # location from the locations-to-visit list.
    # Then we jump back to the while loop and the for loop searches for the closest location to the
    # new current location.
    # The while loop ends when we have visited all the locations.
    def shortest_path_finder(truck_unvisited, truck_num):
        current_location = 0  # Hub

        # Sub-function that adds locations to the visited-locations list, removes locations from
        # the locations-to-visit list, and updates the current location
        def manage_queue(
            truck_pkg_opt, truck_loc_opt, idx
        ):  # idx is package dictionary {}
            truck_pkg_opt.append(idx)  # Add package {} to truck
            truck_loc_opt.append(idx["location_id"])  # Add location to visited list

            pop_idx = truck_unvisited.index(idx)  # Find index of visited location
            truck_unvisited.pop(pop_idx)  # Remove from unvisited list

            nonlocal current_location
            current_location = temp_location  # Update current location

        # Iterate the locations-to-visit list
        while len(truck_unvisited) > 0:
            # Initialize the closest distance to be infinity
            closest_dist = math.inf
            # Initialize the current location to location #0 (hub)
            temp_location = 0

            # Iterate the locations-to-visit list
            for (
                index
            ) in truck_unvisited:  # index is a dictionary { package_id: 1, etc }
                # If the distance between location #1 and location #2 is the less than the current
                # distance, update it
                if (
                    distance_get(current_location, int(index["location_id"]))
                    <= closest_dist
                ):
                    # Update closest distance
                    closest_dist = distance_get(
                        current_location, int(index["location_id"])
                    )
                    # Update temp location
                    temp_location = int(index["location_id"])

            # We found location id of closest node, now we need to find that package dictionary in the array, so we can pass the package dictionary to the manage_queue() function
            # TODO - Update previous for-loop to use enumerate() to access index of package dictionary in unvisited list and get rid of this second for-loop!!!
            # Update the appropriate trucks:
            # 1. Add location to visited-locations list.
            # 2. Remove location from locations-to-visit list
            # Update current_location

            for index in truck_unvisited:
                if (
                    distance_get(current_location, int(index["location_id"]))
                    == closest_dist
                ):
                    if truck_num == 1:
                        manage_queue(
                            truck1_pkg_seq,
                            truck1_loc_seq,
                            index,
                        )

                    elif truck_num == 2:
                        manage_queue(
                            truck2_pkg_seq,
                            truck2_loc_seq,
                            index,
                        )

                    elif truck_num == 3:
                        manage_queue(
                            truck3_pkg_seq,
                            truck3_loc_seq,
                            index,
                        )

        # return truck_unvisited

    # ------------------------------------------------------------------
    # Initialize locations the truck needs to visit with "0", the location ID for the hub
    truck1_loc_seq.insert(0, "0")
    truck2_loc_seq.insert(0, "0")
    truck3_loc_seq.insert(0, "0")


# =================================================================
#                             NOTES
# =================================================================
"""
TO DO 

Create class
class MyDeliverySystem
MyDeliverySystem.run()
Decorator 

--------------------------------------------------------------------
ValueError : I/O operation on closed file
https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file

Outside the with block, the file is closed.

--------------------------------------------------------------------
Python Lists
https://developers.google.com/edu/python/lists

METHODS
list.append(elem) - at end
list.insert(index, elem) - at index
list.extend(list2) - concat list. Alternative: `arr1 + arr2`
list.index(elem)
list.remove(elem)
list.sort()
list.reverse() - mutator
list.pop(index) 

List Slices
slice(start, stop, step)

list = ['a', 'b', 'c', 'd']
print list[1:-1]   ## ['b', 'c']

list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print list         ## ['z', 'c', 'd']

--------------------------------------------------------------------
HOW TO ACCESS INDEX IN FOR-IN LOOP

https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops

Use enumerate() instead of for-in loop

How to loop with indexes in Python
https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

for i in range(len(presidents)):
for num, name in enumerate(presidents, start=1):
for header, rows in zip(headers, columns):

--------------------------------------------------------------------
CLASS METHOD / STATIC METHOD

class method vs static method in Python
https://www.geeksforgeeks.org/class-method-vs-static-method-python/
https://www.tutorialspoint.com/class-method-vs-static-method-in-python

CLASS
- A class method receives the class as implicit first argument, just like an instance method receives the instance.
- A class method is a method which is bound to the class and not the object of the class.
They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.   
- It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances. 

STATIC
- bound to class, not class instance
- does not receive an implicit first argument
- A static method can’t access or modify class state.

https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
CLASS
intend to call it from the class rather than from a class instance

STATIC
behave like plain functions except that you can call them from an instance or the class
used to group functions

--------------------------------------------------------------------
How to convert float into Hours Minutes Seconds?
https://www.olgagoncalves.com/index.php/article/5196537.html
https://docs.python.org/2/library/string.html#formatspec
https://docs.python.org/3/library/string.html#format-string-syntax
https://stackoverflow.com/questions/27496889/converting-a-float-to-hhmm-format/27496953#27496953
https://stackoverflow.com/questions/134934/display-number-with-leading-zeros

divmod(dividend, divisor) = (quotient, remainder)

--------------------------------------------------------------------
COMPARISON: == VS IS
https://realpython.com/courses/python-is-identity-vs-equality

The == operator compares the value, or equality, of two objects, 
whereas the Python is operator checks whether two variables point to the same object in memory. 
In the vast majority of cases, this means you should use the equality operators == and !=, except when you’re comparing to None.


--------------------------------------------------------------------
MY NOTES

variables in open() block seem to be global, not local to the open() block. 

visited-locations = `truck_loc_opt` (truck locations optimized) 
Visited list.
We visited/checked/chose this node, so we add it to the visited list.
Also, sequence of packages that a truck needs to deliver.

locations-to-visit = `truck_unvisited`
Unvisited list. 
These are locations we haven't visited, and we must search this list to find the closest location to our current location. 
This may seem counter intuitive, but it's from the perspective of the algorithm, not from the 
perspective of the truck. 
I.e., it's not locations-to-visit for the truck to make deliveries. 
It's locations-to-visit for the algorithm to find the closest node. 

truck2_undelivered = unvisited list. Same as truck_unvisited. 
[ 
    { package_id: '2', location_id: '9', address: 'some string', deadline: 'EOD', weight: '44', delivery_start: '9:05:00', delivery_status: 'At hub'}, 
    .... 
]

"""
