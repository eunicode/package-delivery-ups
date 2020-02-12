import csv
import datetime

from helper import print_csv
from helper import str_to_timedelta

# Copy distances csv data
# Space complexity = O(N). Time complexity = O(N)
# Open csv file as a text file and get a file object
with open("csv/distance_data.csv") as csv_file:
    # Convert to iterable reader object to list
    csv_reader_dist = csv.reader(csv_file, delimiter=",")
    csv_reader_dist = list(csv_reader_dist)
    # print_csv(csv_reader_dist)

# Copy location csv data
# Space complexity = O(N). Time complexity = O(N)
with open("csv/location_data.csv") as csv_file_location:
    csv_reader_location = csv.reader(csv_file_location, delimiter=",")
    csv_reader_location = list(csv_reader_location)

    # ------------------------------------------------------------------
    # Calculate current total traveled distance
    # Add distance to a distance accumulator variable passed in as an argument
    # Time complexity = O(1)
    def check_distance(row_value, column_value, sum_of_distance):
        # Distance btw loc #1 and loc #2
        distance = csv_reader_dist[row_value][column_value]

        if distance is "":  # Distance btw location #2 to location #1
            distance = csv_reader_dist[column_value][row_value]

        # Add distance to distance accumulator
        sum_of_distance += float(distance)
        return sum_of_distance

    # Find the distance between location #1 and location #2
    # Time complexity = O(1)
    def check_current_distance(row_value, column_value):
        distance = csv_reader_dist[row_value][
            column_value
        ]  # Distance btw loc #1 and loc #2

        if distance is "":
            distance = csv_reader_dist[column_value][
                row_value
            ]  # Distance btw loc #2 and loc #1

        return float(distance)

    # ------------------------------------------------------------------

    # Calculate accumulated time. Also calculate and store time intervals.
    # Time complexity = O(N)
    def check_time(dist, time):
        # Calculate the time it took to travel a distance by using the truck's speed.
        new_time = dist / 18  # miles * (1 hour/18 miles) = hours
        # Take hours float and format it into a string of hours and minutes
        distance_in_minutes = "{0:02.0f}:{1:02.0f}".format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ":00"  # Add seconds to string

        # Add time interval to `time` list
        time.append(final_time)

        sum = datetime.timedelta()
        # Add all the time intervals in `time` list
        for t in time:
            d = str_to_timedelta(t)
            sum += d
        return sum

    # ------------------------------------------------------------------
    # Lists to hold the order of sorted packages
    first_optimized_truck = []
    first_optimized_truck_index_list = []
    second_optimized_truck = []
    second_optimized_truck_index_list = []
    third_optimized_truck = []
    third_optimized_truck_index_list = []

    # Find a sequence of packages to deliver that will minimize the travel distance.
    # This is a single source shortest path algorithm that uses a greedy approach.
    # The algorithm uses a list to store the sequence of packages to deliver, and another list to
    # keep track of delivered packages.
    # The algorithm works by searching for the closest location to its current location.
    # Once it finds the closest location, it adds that location to the visited-locations list, and
    # removes that location from locations-to-visit list.
    # The time complexity is O(N^2) because it has a while loop with a nested for loop.
    # The while loop has a for loop that iterates the locations-to-visit list until it finds the
    # closest location.
    # Once the for loop finds the closest location, it updates the current location and removes that
    # location from the locations-to-visit list.
    # Then we jump back to the while loop and the for loop searches for the closest location to the
    # new current location.
    # The while loop keeps running until the locations-to-visit list is empty.

    def calculate_shortest_distance(
        truck_distance_list, truck_number, current_location
    ):

        # Sub-function that adds locations to the visited-locations list, removes locations from
        # the locations-to-visit list, and updates the current location
        def manage_queue(organized_list, organized_list_index, index):
            organized_list.append(index)
            organized_list_index.append(index["location_id"])
            pop_value = truck_distance_list.index(index)
            truck_distance_list.pop(pop_value)
            nonlocal current_location
            current_location = new_location

        # Iterate the locations-to-visit list
        while len(truck_distance_list) > 0:
            # Initialize the closest distance to the maximum distance in the distance table
            closest_dist = 14.1
            # Initialize the current location to location #0 (hub)
            new_location = 0

            # Iterate the locations-to-visit list
            for index in truck_distance_list:
                # If the distance between location #1 and location #2 is the less than the current
                # distance, update it
                if (
                    check_current_distance(current_location, int(index["location_id"]))
                    <= closest_dist
                ):
                    closest_dist = check_current_distance(
                        current_location, int(index["location_id"])
                    )
                    new_location = int(index["location_id"])

            # Iterate the visited-locations list.
            # The visited-locations list is synonymous to the sequence of packages that a truck needs to deliver.
            # Update the appropriate trucks:
            # 1. Add location to visited-locations list.
            # 2. Remove location from locations-to-visit list
            # Update current_location
            for index in truck_distance_list:
                if (
                    check_current_distance(current_location, int(index["location_id"]))
                    == closest_dist
                ):
                    if truck_number == 1:
                        manage_queue(
                            first_optimized_truck,
                            first_optimized_truck_index_list,
                            index,
                        )

                    elif truck_number == 2:
                        manage_queue(
                            second_optimized_truck,
                            second_optimized_truck_index_list,
                            index,
                        )

                    elif truck_number == 3:
                        manage_queue(
                            third_optimized_truck,
                            third_optimized_truck_index_list,
                            index,
                        )

        return truck_distance_list

    # ------------------------------------------------------------------
    # Initialize locations the truck needs to visit with "0", the location ID for the hub
    first_optimized_truck_index_list.insert(0, "0")
    second_optimized_truck_index_list.insert(0, "0")
    third_optimized_truck_index_list.insert(0, "0")


# =================================================================
#                             NOTES
# =================================================================
"""
TO DO 

Create class
class MyDeliverySystem
MyDeliverySystem.run()

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
MY NOTES

variables in open() block seem to be global, not local

visited-locations = sequence of packages to deliver
locations-to-visit = delivered packages
This may seem counter intuitive, but it's from the perspective of the algorithm, not from the 
perspective of the truck. 
"""
