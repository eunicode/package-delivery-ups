from helper import str_to_timedelta

from hash_table_instance import (
    truck1,
    truck2,
    truck3,
    ht_pkgs,
)

from shortest_path import (
    distance_get,
    distance_accumulate,
    time_accumulate,
    shortest_path_finder,
    truck1_loc_seq,
    truck1_pkg_seq,
    truck2_loc_seq,
    truck2_pkg_seq,
    truck3_loc_seq,
    truck3_pkg_seq,
    csv_reader_location as address_book,
)

# ------------------------------------------------------------------
# Variables to hold copies of unoptimized trucks' packages
truck1_undelivered = []
truck2_undelivered = []
truck3_undelivered = []

# Variables to hold copies of unoptimized trucks' packages' location IDs
truck1_undelivered_loc = []
truck2_undelivered_loc = []
truck3_undelivered_loc = []

departure_times = {
    "first_time": "8:00:00",
    "second_time": "9:05:00",  # Time late packages arrive at hub
    "third_time": "10:30:00",  # Time first truck returns
}

# Variables to hold the times it takes to travel edges
truck1_times = [departure_times["first_time"]]
truck2_times = [departure_times["second_time"]]
truck3_times = [departure_times["third_time"]]

# Variables to hold total distances
truck1_tot_dist = 0
truck2_tot_dist = 0
truck3_tot_dist = 0

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
    truck_opt_loc,
    truck_tot_dist,
    truck_opt_pkg,
    delivery,
    time_list,
):
    for index in range(len(truck_opt_loc)):
        # If we are at the last location, exit for loop
        if index == len(truck_opt_loc) - 1:
            break

        # Calculate the total distance traveled
        # Time complexity = O(1)
        truck_tot_dist = distance_accumulate(
            int(truck_opt_loc[index]),
            int(truck_opt_loc[index + 1]),
            truck_tot_dist,
        )

        # Calculate accumulated time. Also calculate and store time intervals.
        # Time complexity = O(N)
        deliver_package = time_accumulate(
            distance_get(
                int(truck_opt_loc[index]),
                int(truck_opt_loc[index + 1]),
            ),
            time_list,
        )

        # Update the delivery time
        truck_opt_pkg[index]["delivery_status"] = str(deliver_package)

        ht_pkgs.update(
            truck_opt_pkg[index]["package_id"],
            truck_opt_pkg[index],
        )

    return truck_tot_dist


# ------------------------------------------------------------------
# In a single pass, update departure time for packages in truck 1, and add packages to `truck1_undelivered`
# Time complexity = O(N)
for i, package in enumerate(truck1):
    truck1[i]["delivery_start"] = departure_times["first_time"]
    truck1_undelivered.append(truck1[i])

# Map an address to a location ID, and add the location ID to a location ID list
find_loc_id(truck1_undelivered, truck1_undelivered_loc)

# Find a sequence of packages that minimizes the distance traveled
shortest_path_finder(truck1_undelivered, 1)

# Find the distances between locations, and to add the distances up
truck1_tot_dist = find_dist(
    truck1_loc_seq,
    truck1_tot_dist,
    truck1_pkg_seq,
    truck1_undelivered,
    truck1_times,
)

# ------------------------------------------------------------------
# In a single pass, update departure time for packages in truck 2, and add packages to `truck2_undelivered`
# Time complexity = O(N)
for i, pkg in enumerate(truck2):
    truck2[i]["delivery_start"] = departure_times["second_time"]
    truck2_undelivered.append(truck2[i])

# Map an address to a location ID, and add the location ID to a location ID list
find_loc_id(truck2_undelivered, truck2_undelivered_loc)

# Find a sequence of packages that minimizes the distance traveled
shortest_path_finder(truck2_undelivered, 2)

# Find the distances between locations, and to add the distances up
truck2_tot_dist = find_dist(
    truck2_loc_seq,
    truck2_tot_dist,
    truck2_pkg_seq,
    truck2_undelivered,
    truck2_times,
)

# ------------------------------------------------------------------
# In a single pass, update departure time for packages in truck 2, and add packages to `truck2_undelivered`
# Time complexity = O(N)
for i, pkg in enumerate(truck3):
    truck3[i]["delivery_start"] = departure_times["third_time"]
    truck3_undelivered.append(truck3[i])

# Map an address to a location ID, and add the location ID to a location ID list
find_loc_id(truck3_undelivered, truck3_undelivered_loc)

# Find the distances between locations, and to add the distances up
shortest_path_finder(truck3_undelivered, 3)

# Find the distances between locations, and to add the distances up
truck3_tot_dist = find_dist(
    truck3_loc_seq,
    truck3_tot_dist,
    truck3_pkg_seq,
    truck3_undelivered,
    truck3_times,
)

# ------------------------------------------------------------------
# Add up all the distances to get the final total distance
total_distance = truck1_tot_dist + truck2_tot_dist + truck3_tot_dist

# =================================================================
# TESTS


# =================================================================
#                             NOTES
# =================================================================
"""
TO DO

Get rid of globals. Or package them in an array. 
Find a better way to initialize global primitive variables, pass them as arguments to functions, and then update them. 
Currently reassigning values after calling function.

Make a function to calculate third departure time. 
Calculate the time from the distance of last delivery location to hub, and the time of the last delivery. 

Find out why find_loc_id(delivery, dist_list) returns "Address not found!"

Find out how hash table gets updated without this code: 
ht_pkgs.update(truck_opt_pkg[index]["package_id"], truck_opt_pkg[index],)

--------------------------------------------------------------------
DEBUGGER

VS Code and python debugger returning error but can run in the terminal
https://stackoverflow.com/questions/55758072/vs-code-and-python-debugger-returning-error-but-can-run-in-the-terminal

launch.json
"cwd": "${fileDirname}/<WhateverYouWant>"

--------------------------------------------------------------------
SCOPE - NONLOCAL

Functions have their own scope. Functions have their own variables. 
You can pass a global primitive variable as an argument, 
but the function will create its own variable 
that is initialized to that primitive value. 
It does not mutate/update/re-assign/change the global primitive variable.
"""
