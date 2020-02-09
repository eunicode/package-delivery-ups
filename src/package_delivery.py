# import datetime
from helper import str_to_timedelta

from hash_table_instance import check_first_truck_first_trip
from hash_table_instance import check_first_truck_second_trip
from hash_table_instance import check_second_truck_first_trip
from hash_table_instance import get_hash_map
from hash_table_instance import first_truck

import distances

from distances import check_distance
from distances import check_time_first_truck
from distances import check_time_second_truck
from distances import check_time_third_truck
from distances import check_current_distance
from distances import calculate_shortest_distance
from distances import first_optimized_truck_index
from distances import first_optimized_truck_list
from distances import second_optimized_truck_index
from distances import second_optimized_truck_list
from distances import third_optimized_truck_index
from distances import third_optimized_truck_list


first_delivery = []
second_delivery = []
third_delivery = []

first_truck_distance_list = []
second_truck_distance_list = []
third_truck_distance_list = []

# this is the time that the first truck leaves the hub
first_time_list = ["8:00:00"]
second_time_list = ["9:10:00"]
third_time_list = ["11:00:00"]

departure_times = {
    "first_time": "8:00:00",
    "second_time": "9:10:00",
    "third_time": "11:00:00",
}

# the times below represent the times that each truck leaves the hub
# first_time = "8:00:00"
# Drivers leave the hub at 8am
# second_time = "9:10:00"
# third_time = "11:00:00"
# 9am - deadline 1
# 10:30 - deadline 2
# 9:05 - package arrives in hub
# 10:20 am - time package 9 address is corrected

# the operations below convert the string time into a datetime.timedelta
# first_time
convert_first_time = str_to_timedelta(departure_times["first_time"])

# (hour, min, sec) = second_time.split(":")
# convert_second_time = datetime.timedelta(
#     hours=int(hour), minutes=int(min), seconds=int(sec)
# )
convert_second_time = str_to_timedelta(departure_times["second_time"])
# (hour, min, sec) = third_time.split(":")
# convert_third_time = datetime.timedelta(
#     hours=int(hour), minutes=int(min), seconds=int(sec)
# )
convert_third_time = str_to_timedelta(departure_times["third_time"])
# =================================================================

# for loop updates the delivery status of all packages in truck 1 to when the truck leaves the station
# counter to iterate through for loop
# i = 0
# # Space-time complexity is O(N)
# for value in check_first_truck_first_trip():
#     check_first_truck_first_trip()[i][
#         9
#     ] = first_time  # Update delivery start to package in first_truck
#     first_delivery.append(
#         check_first_truck_first_trip()[i]
#     )  # Add package to `first_delivery` list
#     i += 1
for i, package in enumerate(first_truck):
    first_truck[i][9] = "8:00:00"
    first_delivery.append(first_truck[i])

# this for loop compares the addresses on truck one, to the list of addresses, and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    first_variable_count = 0
    address_book = distances.check_address()

    for pkg in first_delivery:
        for location in address_book:
            if pkg[2] == location[2]:  # If package address matches a location
                first_truck_distance_list.append(
                    location[0]
                )  # Add location ID to `first_truck_distance_list`
                first_delivery[first_variable_count][1] = location[
                    0
                ]  # Add location ID to package data
        first_variable_count += 1
except IndexError:
    pass

# calls to the greedy algorithm that sorts the packages in a more efficient order
print("hi")
calculate_shortest_distance(first_delivery, 1, 0)
first_truck_total_distance = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
first_truck_package_id = 0
for index in range(len(first_optimized_truck_index())):
    try:
        # calculate the total distance of the truck
        first_truck_total_distance = check_distance(
            int(first_optimized_truck_index()[index]),
            int(first_optimized_truck_index()[index + 1]),
            first_truck_total_distance,
        )

        # calculate the distance of each package along the route
        deliver_package = check_time_first_truck(
            check_current_distance(
                int(first_optimized_truck_index()[index]),
                int(first_optimized_truck_index()[index + 1]),
            ),
            first_time_list,
        )

        first_optimized_truck_list()[first_truck_package_id][10] = str(deliver_package)

        get_hash_map().update(
            int(first_optimized_truck_list()[first_truck_package_id][0]), first_delivery
        )

        first_truck_package_id += 1

    except IndexError:
        pass

# =================================================================
# for loop updates the delivery status of all packages in truck 2 to when they leave the station
i = 0  # counter to iterate through for loop
# Space-time complexity is O(N)
for value in check_second_truck_first_trip():
    check_second_truck_first_trip()[i][9] = departure_times["second_time"]
    # check_second_truck_first_trip()[i][9] = second_time
    second_delivery.append(check_second_truck_first_trip()[i])
    i += 1

# this for loop compares the addresses on truck two to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    second_variable_count = 0
    for k in second_delivery:
        for j in distances.check_address():
            if k[2] == j[2]:
                second_truck_distance_list.append(j[0])
                second_delivery[second_variable_count][1] = j[0]
        second_variable_count += 1
except IndexError:
    pass

# calls to the greedy algorithm that sorts the packages in a more efficient order
calculate_shortest_distance(second_delivery, 2, 0)
second_truck_total_distance = 0

# this for loop takes the values in the second truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
second_truck_package_id = 0
for index in range(len(second_optimized_truck_index())):
    try:
        # calculate the total distance of the truck
        second_truck_total_distance = check_distance(
            int(second_optimized_truck_index()[index]),
            int(second_optimized_truck_index()[index + 1]),
            second_truck_total_distance,
        )
        # calculate the distance of each package along the route
        deliver_package = check_time_second_truck(
            check_current_distance(
                int(second_optimized_truck_index()[index]),
                int(second_optimized_truck_index()[index + 1]),
            ),
            second_time_list,
        )
        second_optimized_truck_list()[second_truck_package_id][10] = str(
            deliver_package
        )
        get_hash_map().update(
            int(second_optimized_truck_list()[second_truck_package_id][0]),
            second_delivery,
        )
        second_truck_package_id += 1
    except IndexError:
        pass

# =================================================================
# for loop updates the delivery status of all packages in truck 1 (second delivery) to 'In transit'
i = 0
# Space-time complexity is O(N)
for value in check_first_truck_second_trip():
    check_first_truck_second_trip()[i][9] = departure_times["third_time"]
    # check_first_truck_second_trip()[i][9] = third_time
    third_delivery.append(check_first_truck_second_trip()[i])
    i += 1

# this for loop compares the addresses on truck one (second delivery) to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    third_variable_count = 0
    for k in third_delivery:
        for j in distances.check_address():
            if k[2] == j[2]:
                third_truck_distance_list.append(j[0])
                third_delivery[third_variable_count][1] = j[0]
        third_variable_count += 1
except IndexError:
    pass

# calls to the greedy algorithm that sorts the packages in a more efficient order
calculate_shortest_distance(third_delivery, 3, 0)
third_truck_total_distance = 0
# this for loop takes the values in the third truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
third_truck_package_id = 0
for index in range(len(third_optimized_truck_index())):
    try:
        # calculate the total distance of the truck
        third_truck_total_distance = check_distance(
            int(third_optimized_truck_index()[index]),
            int(third_optimized_truck_index()[index + 1]),
            third_truck_total_distance,
        )
        # calculate the distance of each package along the route
        deliver_package = check_time_third_truck(
            check_current_distance(
                int(third_optimized_truck_index()[index]),
                int(third_optimized_truck_index()[index + 1]),
            ),
            third_time_list,
        )
        third_optimized_truck_list()[third_truck_package_id][10] = str(deliver_package)
        get_hash_map().update(
            int(third_optimized_truck_list()[third_truck_package_id][0]), third_delivery
        )
        third_truck_package_id += 1
    except IndexError:
        pass

# =================================================================
# function returns total distance of all 3 trips to calculate the distance of all packages
# Space-time complexity is O(1)
def total_distance():
    total_distance = (
        first_truck_total_distance
        + second_truck_total_distance
        + third_truck_total_distance
    )
    return total_distance


# =================================================================
#                             NOTES
# =================================================================
"""
VS Code and python debugger returning error but can run in the terminal
https://stackoverflow.com/questions/55758072/vs-code-and-python-debugger-returning-error-but-can-run-in-the-terminal

launch.json
"cwd": "${fileDirname}/<WhateverYouWant>"
--------------------------------------------------------------------
"""
