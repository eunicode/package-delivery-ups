from helper import str_to_timedelta

from hash_table_instance import (
    first_truck,
    second_truck,
    third_truck,
    ht_pkgs,
)

from shortest_path import (
    check_distance,
    check_time,
    check_current_distance,
    calculate_shortest_distance,
    first_optimized_truck_index_list,
    first_optimized_truck,
    second_optimized_truck_index_list,
    second_optimized_truck,
    third_optimized_truck_index_list,
    third_optimized_truck,
    csv_reader_location as address_book,
)

# ------------------------------------------------------------------
first_delivery = []
second_delivery = []
third_delivery = []

first_truck_distance_list = []
second_truck_distance_list = []
third_truck_distance_list = []

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

convert_first_time = str_to_timedelta(departure_times["first_time"])

convert_second_time = str_to_timedelta(departure_times["second_time"])

convert_third_time = str_to_timedelta(departure_times["third_time"])

# ------------------------------------------------------------------
# Function to map an address to a location ID, and add the location ID to a location ID list
# Time complexity is O(N^2)
def find_loc_id(delivery, dist_list):
    for i, pkg in enumerate(delivery):
        for location in address_book:
            # If package address matches a location
            if pkg["address"] == location[2]:  # loc address
                # Add location ID to truck list
                dist_list.append(location[0])  # loc id
                # Add location ID to package data
                delivery[i]["location_id"] = location[0]
                break


# ------------------------------------------------------------------
# Function to find the distances between locations, add the distances up
# Time complexity = O(N^2)
def find_dist(
    opt_truck_idx, truck_tot_dist, opt_truck_list, delivery, truck_pkg_id, time_list,
):
    for index in range(len(opt_truck_idx)):
        # If we are at the last location, exit for loop
        if index == len(opt_truck_idx) - 1:
            break

        # Calculate the total distance traveled
        # Time complexity = O(1)
        truck_tot_dist = check_distance(
            int(opt_truck_idx[index]), int(opt_truck_idx[index + 1]), truck_tot_dist,
        )

        # Calculate accumulated time. Also calculate and store time intervals.
        # Time complexity = O(N)
        deliver_package = check_time(
            check_current_distance(
                int(opt_truck_idx[index]), int(opt_truck_idx[index + 1]),
            ),
            time_list,
        )

        # Update the delivery time
        opt_truck_list[truck_pkg_id]["delivery_status"] = str(deliver_package)

        ht_pkgs.update(
            opt_truck_list[truck_pkg_id]["package_id"], opt_truck_list[truck_pkg_id],
        )

        truck_pkg_id += 1

    return truck_tot_dist


# ------------------------------------------------------------------
# In a single pass, update departure time for packages in truck 1, and add packages to `first_delivery`
# Time complexity = O(N)
for i, package in enumerate(first_truck):
    first_truck[i]["delivery_start"] = departure_times["first_time"]
    first_delivery.append(first_truck[i])

# Map an address to a location ID, and add the location ID to a location ID list
find_loc_id(first_delivery, first_truck_distance_list)

# Find a sequence of packages that minimizes the distance traveled
calculate_shortest_distance(first_delivery, 1, 0)


# this for loop takes the values in the first truck and runs them through the distance functions in the distances.py file

# Find the distances between locations, and to add the distances up
first_truck_total_distance = find_dist(
    first_optimized_truck_index_list,
    first_truck_total_distance,
    first_optimized_truck,
    first_delivery,
    first_truck_package_id,
    first_time_list,
)

# ------------------------------------------------------------------
# In a single pass, update departure time for packages in truck 2, and add packages to `second_delivery`
# Time complexity = O(N)
for i, pkg in enumerate(second_truck):
    second_truck[i]["delivery_start"] = departure_times["second_time"]
    second_delivery.append(second_truck[i])

# Map an address to a location ID, and add the location ID to a location ID list
find_loc_id(second_delivery, second_truck_distance_list)

# Find a sequence of packages that minimizes the distance traveled
calculate_shortest_distance(second_delivery, 2, 0)

# Find the distances between locations, and to add the distances up
second_truck_total_distance = find_dist(
    second_optimized_truck_index_list,
    second_truck_total_distance,
    second_optimized_truck,
    second_delivery,
    second_truck_package_id,
    second_time_list,
)

# ------------------------------------------------------------------
# In a single pass, update departure time for packages in truck 2, and add packages to `second_delivery`
# Time complexity = O(N)
for i, pkg in enumerate(third_truck):
    third_truck[i]["delivery_start"] = departure_times["third_time"]
    third_delivery.append(third_truck[i])

# Map an address to a location ID, and add the location ID to a location ID list
find_loc_id(third_delivery, third_truck_distance_list)

# Find the distances between locations, and to add the distances up
calculate_shortest_distance(third_delivery, 3, 0)

# Find the distances between locations, and to add the distances up
third_truck_total_distance = find_dist(
    third_optimized_truck_index_list,
    third_truck_total_distance,
    third_optimized_truck,
    third_delivery,
    third_truck_package_id,
    third_time_list,
)

# ------------------------------------------------------------------
# Add up all the distances to get the final total distance
# Time complexity = O(1)
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

Find out why find_loc_id(delivery, dist_list) returns "Address not found!"

Find out how hash table gets updated without this code: 
ht_pkgs.update(opt_truck_list[truck_pkg_id]["package_id"], opt_truck_list[truck_pkg_id],)

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
