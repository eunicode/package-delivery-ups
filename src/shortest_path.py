import csv
import datetime

from helper import print_csv
from helper import str_to_timedelta

# Read in csv file that is the mapping of distances between locations
with open("csv/distance_data.csv") as csv_file:
    # Convert to iterable reader object to list
    # CSV_READER = list(csv.reader(csv_file, delimiter=","))
    csv_reader_dist = csv.reader(csv_file, delimiter=",")
    csv_reader_dist = list(csv_reader_dist)
    # print_csv(csv_reader_dist)

# Read in csv file that is the names of all possible delivery locations
with open("csv/location_data.csv") as csv_file_location:
    csv_reader_location = csv.reader(csv_file_location, delimiter=",")
    # print_csv(csv_reader_location)
    csv_reader_location = list(csv_reader_location)
    # print_csv(csv_reader_location)

    # ------------------------------------------------------------------
    # a list of row/column values are inserted into this function.
    # This function then calculates the total distance
    # that distance is then returned, and each iteration represents a distance between two locations
    # Space-time complexity is O(1)
    def check_distance(row_value, column_value, sum_of_distance):
        distance = csv_reader_dist[row_value][column_value]  # hub to location

        if distance is "":  # location to hub
            distance = csv_reader_dist[column_value][row_value]

        sum_of_distance += float(distance)
        return sum_of_distance

    # this function is very similar to the function above but returns a current distance
    # Space-time complexity is O(1)
    def check_current_distance(row_value, column_value):
        distance = csv_reader_dist[row_value][column_value]

        if distance is "":
            distance = csv_reader_dist[column_value][row_value]

        return float(distance)

    # ------------------------------------------------------------------
    # this is the time that the first truck leaves the hub
    # first_time_list = ["8:00:00"]
    # second_time_list = ["9:10:00"]
    # third_time_list = ["11:00:00"]

    # this function takes a distance then divides it by 18. It then uses divmod to display a time, and appends 00
    # this string that is a timestamp is then split, and turned into a datetime timedelta object
    # that object is then added to sum which represents total distance for a particular truck
    # runtime of function is O(N)

    def check_time(dist, time):
        new_time = dist / 18  # miles * (1 hour/18 miles) = hours
        # new_time = distance / 18
        distance_in_minutes = "{0:02.0f}:{1:02.0f}".format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ":00"
        time.append(final_time)
        # first_time_list.append(final_time)
        # second_time_list.append(final_time)
        # third_time_list.append(final_time)
        sum = datetime.timedelta()

        for t in time:
            # for i in first_time_list:
            # for i in third_time_list:
            # (hour, min, sec) = t.split(":")
            # d = datetime.timedelta(hours=int(hour), minutes=int(min), seconds=int(sec))
            d = str_to_timedelta(t)
            sum += d

        return sum

    # def check_time_first_truck(distance, time_list):
    #     return check_time(distance, time_list)

    # Repeated function for second truck
    # def check_time_second_truck(distance, time_list):
    #     return check_time(distance, time_list)

    # Repeated function for the third truck
    # def check_time_third_truck(distance, time_list):
    #     return check_time(distance, time_list)

    # ------------------------------------------------------------------
    # this function returns the time objects to use in the Packages.py file
    # Space-time complexity is O(1)
    # def check_address():
    #     return csv_reader_location

    # ------------------------------------------------------------------
    # these lists represent the sorted trucks that are put in order of efficiency in the function below
    first_optimized_truck = []
    first_optimized_truck_index_list = []
    second_optimized_truck = []
    second_optimized_truck_index_list = []
    third_optimized_truck = []
    third_optimized_truck_index_list = []

    # This is my sorting algorithm that uses a greedy approach to automate optimizing the delivery route for each truck.
    # the function takes 3 parameters (see section 1)
    # First parameter is the list of packages on a truck that has not been optimized yet
    # The second parameter represents the truck number
    # The third parameter represents the current location that is updated each time a truck moves

    # The base case of the algorithm is stated in the initial if statement (see section 2).
    # This breaks the recursion once the input list has a size of 0.
    # It starts by setting a "lowest value" of 50.0
    # and then uses the check current distance function to loop through every possible point that is currently available to see if there is a lower value.
    # If there is than the lowest value is updated and the search continues (see section 3).
    # Once it has searched through all possible routes the truck can go given the available packages,
    # it then adds that package object and associated index to new lists (see section 4).
    # To ensure that the right truck packages are being associated, the second parameter is checked.
    # If the truck truck is being sorted than the optimized delivery path will be associated to the lists first_optimized_truck and first_optimized_truck_index.
    # Each time these lists are updated, the lowest value is removed from the argument list, truck_distance_list.
    # This will allow us to update current location and recursively call the function.
    # Once the argument list is empty it will return the empty list and the function call will end.

    # The space-time complexity of this algorithm is O(N^2).
    # This is due to the two for loops and the repeated lookup functionality required to determine the lowest possible path then move the truck to that position.

    def calculate_shortest_distance(
        truck_distance_list, truck_number, current_location
    ):

        # Sorting algo helper function
        def manage_queue(organized_list, organized_list_index, index):
            organized_list.append(index)
            # organized_list_index.append(index[1])
            organized_list_index.append(index["location_id"])
            pop_value = truck_distance_list.index(index)
            truck_distance_list.pop(pop_value)
            nonlocal current_location
            current_location = new_location

        # section 1
        # if len(truck_distance_list) == 0:  # section 2
        #     return truck_distance_list

        # update variables

        while len(truck_distance_list) > 0:
            closest_dist = 14.1  # maximum distance in distances table
            new_location = 0

            for index in truck_distance_list:
                if (
                    # check_current_distance(current_location, int(index[1]))
                    check_current_distance(current_location, int(index["location_id"]))
                    <= closest_dist
                ):
                    closest_dist = check_current_distance(
                        current_location,
                        int(index["location_id"])
                        # current_location, int(index[1])
                    )  # section 3
                    new_location = int(index["location_id"])
                    # new_location = int(index[1])

            # Add package to optimized package list
            # Remove package from packages to check
            # Update current_location
            for index in truck_distance_list:  # section 4
                # current_location = 0

                if (
                    # check_current_distance(current_location, int(index[1]))
                    check_current_distance(current_location, int(index["location_id"]))
                    == closest_dist
                ):
                    if truck_number == 1:
                        # replace
                        # first_optimized_truck.append(index)
                        # first_optimized_truck_index_list.append(index[1])
                        # pop_value = truck_distance_list.index(index)
                        # truck_distance_list.pop(pop_value)
                        # current_location = new_location
                        manage_queue(
                            first_optimized_truck,
                            first_optimized_truck_index_list,
                            index,
                        )
                        # calculate_shortest_distance(
                        #     truck_distance_list, 1, current_location
                        # )

                    elif truck_number == 2:
                        # replace
                        # second_optimized_truck.append(index)
                        # second_optimized_truck_index_list.append(index[1])
                        # pop_value = truck_distance_list.index(index)
                        # truck_distance_list.pop(pop_value)
                        # current_location = new_location
                        manage_queue(
                            second_optimized_truck,
                            second_optimized_truck_index_list,
                            index,
                        )
                        # calculate_shortest_distance(
                        #     truck_distance_list, 2, current_location
                        # )
                    elif truck_number == 3:
                        # replace
                        # third_optimized_truck.append(index)
                        # third_optimized_truck_index_list.append(index[1])
                        # pop_value = truck_distance_list.index(index)
                        # truck_distance_list.pop(pop_value)
                        # current_location = new_location
                        manage_queue(
                            third_optimized_truck,
                            third_optimized_truck_index_list,
                            index,
                        )
                        # calculate_shortest_distance(
                        #     truck_distance_list, 3, current_location
                        # )

        return truck_distance_list

    # ------------------------------------------------------------------

    first_optimized_truck_index_list.insert(0, "0")

    # Space-time complexity is O(1)
    # def first_optimized_truck_index():
    #     return first_optimized_truck_index_list

    # Space-time complexity is O(1)
    # def first_optimized_truck_list():
    #     return first_optimized_truck

    second_optimized_truck_index_list.insert(0, "0")

    # Space-time complexity is O(1)
    # def second_optimized_truck_index():
    #     return second_optimized_truck_index_list

    # Space-time complexity is O(1)
    # def second_optimized_truck_list():
    #     return second_optimized_truck

    third_optimized_truck_index_list.insert(0, "0")

    # Space-time complexity is O(1)
    # def third_optimized_truck_index():
    #     return third_optimized_truck_index_list

    # Space-time complexity is O(1)
    # def third_optimized_truck_list():
    #     return third_optimized_truck


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

variables in open block seem to be global, not local
"""
