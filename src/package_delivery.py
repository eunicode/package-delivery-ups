# import datetime
from helper import str_to_timedelta

from hash_table_instance import (
    first_truck,
    second_truck,
    third_truck,
    ht_pkgs,
)

# from hash_table_instance import check_first_truck_first_trip
# from hash_table_instance import check_first_truck_second_trip

# from hash_table_instance import check_second_truck_first_trip
# from hash_table_instance import get_hash_map


# import shortest_path

from shortest_path import (
    check_distance,
    check_time,
    # check_time_first_truck,
    # check_time_second_truck,
    # check_time_third_truck,
    check_current_distance,
    calculate_shortest_distance,
    # first_optimized_truck_index,
    first_optimized_truck_index_list,
    # first_optimized_truck_list,
    first_optimized_truck,
    # second_optimized_truck_index,
    second_optimized_truck_index_list,
    # second_optimized_truck_list,
    second_optimized_truck,
    # third_optimized_truck_index,
    third_optimized_truck_index_list,
    # third_optimized_truck_list,
    third_optimized_truck,
    csv_reader_location as address_book,
)


first_delivery = []
second_delivery = []
third_delivery = []

first_truck_distance_list = []
second_truck_distance_list = []
third_truck_distance_list = []

# this is the time that the first truck leaves the hub
departure_times = {
    "first_time": "8:00:00",
    "second_time": "9:10:00",
    "third_time": "11:00:00",
}

first_time_list = [departure_times["first_time"]]
second_time_list = [departure_times["second_time"]]
third_time_list = [departure_times["third_time"]]

first_truck_total_distance = 0
first_truck_package_id = 0
second_truck_total_distance = 0
second_truck_package_id = 0
third_truck_total_distance = 0
third_truck_package_id = 0

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


def find_loc_id(delivery, dist_list):
    for i, pkg in enumerate(delivery):
        for location in address_book:
            # If package address matches a location
            if pkg["address"] == location[2]:  # loc address
                # Add location ID to truck list
                dist_list.append(location[0])  # loc id
                # Add location ID to package data
                delivery[i]["location_id"] = location[0]


def find_dist(
    opt_truck_idx,
    truck_tot_dist,
    opt_truck_list,
    delivery,
    truck_pkg_id,
    time_list,
    # check_time,
):
    for index in range(len(opt_truck_idx)):
        # If we are at the last location, exit for loop
        if index == len(opt_truck_idx) - 1:
            break
        # try:
        # calculate the total distance of the truck
        truck_tot_dist = check_distance(
            int(opt_truck_idx[index]), int(opt_truck_idx[index + 1]), truck_tot_dist,
        )

        # calculate the distance of each package along the route
        deliver_package = check_time(
            check_current_distance(
                int(opt_truck_idx[index]), int(opt_truck_idx[index + 1]),
            ),
            time_list,
        )

        opt_truck_list[truck_pkg_id]["delivery_status"] = str(deliver_package)

        # ht_pkgs.update(
        #     opt_truck_list[truck_pkg_id]["package_id"], opt_truck_list[truck_pkg_id],
        # )
        # ht_pkgs.update(
        #     int(opt_truck_list[truck_pkg_id]["package_id"]), delivery,
        # )

        truck_pkg_id += 1
        # except IndexError:
        #     pass
    return truck_tot_dist


# =================================================================

# for loop updates the delivery status of all packages in truck 1 to when the truck leaves the station
# Space-time complexity is O(N)
# In a single pass, update departure time for packages in truck 1,
# and add packages to `first_delivery`
for i, package in enumerate(first_truck):
    first_truck[i]["delivery_start"] = departure_times["first_time"]
    first_delivery.append(first_truck[i])

# this for loop compares the addresses on truck one, to the list of addresses, and adds the address index to the list
# Space-time complexity is O(N^2)
find_loc_id(first_delivery, first_truck_distance_list)
# try:
#     first_variable_count = 0

#     for pkg in first_delivery:
#         for location in address_book:
#             # If package address matches a location
#             if pkg["address"] == location[2]:
#                 # Add location ID to truck list
#                 first_truck_distance_list.append(location[0])
#                 # Add location ID to package data
#                 first_delivery[first_variable_count]["location_id"] = location[0]
#         first_variable_count += 1
# except IndexError:
#     pass

# calls to the greedy algorithm that sorts the packages in a more efficient order
calculate_shortest_distance(first_delivery, 1, 0)
# first_truck_total_distance = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
# first_truck_package_id = 0

first_truck_total_distance = find_dist(
    first_optimized_truck_index_list,
    first_truck_total_distance,
    first_optimized_truck,
    first_delivery,
    first_truck_package_id,
    first_time_list,
    # check_time_first_truck,
)
# for index in range(len(first_optimized_truck_index())):
#     try:
#         # calculate the total distance of the truck
#         first_truck_total_distance = check_distance(
#             int(first_optimized_truck_index()[index]),
#             int(first_optimized_truck_index()[index + 1]),
#             first_truck_total_distance,
#         )

#         # calculate the distance of each package along the route
#         deliver_package = check_time_first_truck(
#             check_current_distance(
#                 int(first_optimized_truck_index()[index]),
#                 int(first_optimized_truck_index()[index + 1]),
#             ),
#             first_time_list,
#         )

#         first_optimized_truck_list()[first_truck_package_id]["delivery_status"] = str(
#             deliver_package
#         )

#         insert_into_hash_table.update(
#             int(first_optimized_truck_list()[first_truck_package_id]["package_id"]),
#             first_delivery,
#         )

#         first_truck_package_id += 1

#     except IndexError:
#         pass

# =================================================================
# for loop updates the delivery status of all packages in truck 2 to when they leave the station
# Space-time complexity is O(N)
for i, pkg in enumerate(second_truck):
    second_truck[i]["delivery_start"] = departure_times["second_time"]
    second_delivery.append(second_truck[i])

# this for loop compares the addresses on truck two to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
find_loc_id(second_delivery, second_truck_distance_list)

# calls to the greedy algorithm that sorts the packages in a more efficient order
calculate_shortest_distance(second_delivery, 2, 0)
# second_truck_total_distance = 0

# this for loop takes the values in the second truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)
# second_truck_package_id = 0

second_truck_total_distance = find_dist(
    second_optimized_truck_index_list,
    second_truck_total_distance,
    second_optimized_truck,
    second_delivery,
    second_truck_package_id,
    second_time_list,
    # check_time_second_truck,
)
# for index in range(len(second_optimized_truck_index())):
#     try:
#         # calculate the total distance of the truck
#         second_truck_total_distance = check_distance(
#             int(second_optimized_truck_index()[index]),
#             int(second_optimized_truck_index()[index + 1]),
#             second_truck_total_distance,
#         )
#         # calculate the distance of each package along the route
#         deliver_package = check_time_second_truck(
#             check_current_distance(
#                 int(second_optimized_truck_index()[index]),
#                 int(second_optimized_truck_index()[index + 1]),
#             ),
#             second_time_list,
#         )
#         second_optimized_truck_list()[second_truck_package_id]["delivery_status"] = str(
#             deliver_package
#         )
#         insert_into_hash_table.update(
#             int(second_optimized_truck_list()[second_truck_package_id]["package_id"]),
#             second_delivery,
#         )
#         second_truck_package_id += 1
#     except IndexError:
#         pass
# =================================================================
# for loop updates the delivery status of all packages in truck 1 (second delivery) to 'In transit'
# Space-time complexity is O(N)
for i, pkg in enumerate(third_truck):
    third_truck[i]["delivery_start"] = departure_times["third_time"]
    third_delivery.append(third_truck[i])

# this for loop compares the addresses on truck one (second delivery) to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
find_loc_id(third_delivery, third_truck_distance_list)

# calls to the greedy algorithm that sorts the packages in a more efficient order
calculate_shortest_distance(third_delivery, 3, 0)

# this for loop takes the values in the third truck and runs them through the distance functions in the distances.py file
# Space-time complexity is O(N)

third_truck_total_distance = find_dist(
    third_optimized_truck_index_list,
    third_truck_total_distance,
    third_optimized_truck,
    third_delivery,
    third_truck_package_id,
    third_time_list,
    # check_time_third_truck,
)
# for index in range(len(third_optimized_truck_index())):
#     try:
#         # calculate the total distance of the truck
#         third_truck_total_distance = check_distance(
#             int(third_optimized_truck_index()[index]),
#             int(third_optimized_truck_index()[index + 1]),
#             third_truck_total_distance,
#         )
#         # calculate the distance of each package along the route
#         deliver_package = check_time_third_truck(
#             check_current_distance(
#                 int(third_optimized_truck_index()[index]),
#                 int(third_optimized_truck_index()[index + 1]),
#             ),
#             third_time_list,
#         )
#         third_optimized_truck_list()[third_truck_package_id]["delivery_status"] = str(
#             deliver_package
#         )
#         insert_into_hash_table.update(
#             int(third_optimized_truck_list()[third_truck_package_id]["package_id"]),
#             third_delivery,
#         )
#         third_truck_package_id += 1
#     except IndexError:
#         pass

# =================================================================
# first_truck_total distance = find_dist
# first_truck_package_id = 0
# second_truck_total_distance = 0
# second_truck_package_id = 0
# third_truck_total_distance = 0
# third_truck_package_id = 0

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
# TESTS

# print(first_truck_total_distance)
# truck_location_list = first_optimized_truck_index()
# print(truck_location_list)
# truck_package_list = first_optimized_truck_list()
# print(truck_package_list)

# print(f"first delivery: {first_delivery}")
# print(f"first truck: {first_truck}")

# print(first_truck_package_id)

# =================================================================
#                             NOTES
# =================================================================
"""
TO DO

Get rid of globals. Or package them in an array. 
Find a better way to initialize global primitive variables, pass them as arguments to functions,
and then update them. Currently reassigning values after calling function.

Make a function to calculate third departure time. Calculate the time from the distance of last 
delivery location to hub, and the time of the last delivery. 

--------------------------------------------------------------------
VS Code and python debugger returning error but can run in the terminal
https://stackoverflow.com/questions/55758072/vs-code-and-python-debugger-returning-error-but-can-run-in-the-terminal

launch.json
"cwd": "${fileDirname}/<WhateverYouWant>"

--------------------------------------------------------------------
Functions have their own scope. Functions have their own variables. 
You can pass a global primitive variable as an argument, but the function will create its own variable 
that is initialized to that primitive value. It does not mutate the global primitive variable.
"""
