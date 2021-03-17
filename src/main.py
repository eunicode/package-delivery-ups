from hash_table_instance import ht_pkgs
from package_delivery import total_distance
from helper import interface_print, str_to_timedelta, interface_print_single

print("Welcome to the package delivery system!\n")

print(f"All packages were delivered in {total_distance} miles.")

# -------------------------------------------------------------------
# The time complexity for printing all packages is O(N)
# The time complexity for printing one package is O(1)
while True:
    # Store user input in `command` and display interface menu options
    command = input(
        """
    =================================================================
    MENU:
    Enter "lookup" to lookup a package by its ID.
    Enter "status" to view the delivery status of all packages.
    Enter "exit" to exit program.
    =================================================================
    \nEnter a command:
    """
    )
    # This code block prints data for all packages
    # This code block has a time complexity of O(N) bc it will iterate all the packages in the hash table.
    # Inside the for loop we have a get() operation which has a time complexity of O(1).
    if command == "status":
        input_time = input("Enter a time in the HH:MM:SS format: ")
        convert_input_time = str_to_timedelta(input_time)

        # Run code block for every package
        for id in range(1, 41):
            # Get times from the hash table
            departure = ht_pkgs.get(str(id))["delivery_start"]
            arrival = ht_pkgs.get(str(id))["delivery_status"]

            # Convert strings to timedelta
            convert_departure = str_to_timedelta(departure)
            convert_arrival = str_to_timedelta(arrival)

            # First checks all packages against the given time determine if they have left the hub yet.
            # If the user input time is earlier than the departure time, the package is in the hub.
            if convert_input_time <= convert_departure:
                ht_pkgs.get(str(id))["delivery_start"] = "Leaves at " + departure
                ht_pkgs.get(str(id))["delivery_status"] = "At hub"

                # Print package data
                interface_print_single(id)

            # If user input time is later than the departure time, the package is either in transit
            # or delivered.
            elif convert_input_time >= convert_departure:
                # If user input time is before the delivery time, the package is in transit
                if convert_input_time < convert_arrival:
                    ht_pkgs.get(str(id))["delivery_start"] = "Left at " + departure
                    ht_pkgs.get(str(id))["delivery_status"] = "In transit"

                    # Print package data
                    interface_print_single(id)

                # If user input time is after the delivery time, the package is delivered
                else:
                    ht_pkgs.get(str(id))["delivery_start"] = "Left at " + departure
                    ht_pkgs.get(str(id))["delivery_status"] = "Delivered at " + arrival

                    # Print package data
                    interface_print_single(id)

    # -------------------------------------------------------------------
    # This code block prints data for a user specified package
    # This code block is O(1) bc the operations in this code block, such as the get() operation, is O(1)
    elif command == "lookup":
        id = input("Enter a package ID to lookup: ")  # package ids 1-40
        departure = ht_pkgs.get(str(id))["delivery_start"]
        arrival = ht_pkgs.get(str(id))["delivery_status"]
        input_time = input("Enter a time as HH:MM:SS: ")

        convert_input_time = str_to_timedelta(input_time)
        convert_departure = str_to_timedelta(departure)
        convert_arrival = str_to_timedelta(arrival)

        # If user input time is earlier than the departure time, the package is at the hub.
        if convert_input_time <= convert_departure:
            ht_pkgs.get(str(id))["delivery_start"] = "Leaves at " + departure
            ht_pkgs.get(str(id))["delivery_status"] = "At hub"

            # Print package data
            interface_print_single(id)

        # If the user input time is later than the departure time:
        elif convert_input_time >= convert_departure:
            # If the user input time is before the delivery time, the package is in transit
            if convert_input_time < convert_arrival:
                ht_pkgs.get(str(id))["delivery_start"] = "Left at " + departure
                ht_pkgs.get(str(id))["delivery_status"] = "In transit"

                # Print package data
                interface_print_single(id)

            # If the user input time is after the delivery time, the package is delivered
            else:
                ht_pkgs.get(str(id))["delivery_start"] = "Left at " + departure
                ht_pkgs.get(str(id))["delivery_status"] = "Delivered at " + arrival

                # Print package data
                interface_print_single(id)

    # -------------------------------------------------------------------
    elif command == "exit":
        exit()
    # -------------------------------------------------------------------
    else:
        print("Invalid command")
        exit()

# =================================================================
#                             NOTES
# =================================================================
"""
TIMEDELTA 
https://www.geeksforgeeks.org/python-datetime-timedelta-function/
https://www.programiz.com/python-programming/datetime
https://www.guru99.com/date-time-and-datetime-classes-in-python.html

--------------------------------------------------------------------
Multiple assignment and tuple unpacking improve Python code readability
https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/

--------------------------------------------------------------------
ValueError: invalid literal for int() with base 10: 'Left at 9'
--------------------------------------------------------------------
TO DO

Create an Interface class or function
Don't add additional text to delivery_start or delivery_status key values
Create tests to make sure hash table is being updated correctly, 
the shortest path algo is working correctly, etc.

Package IDs from 1-40
Trucks start leaving at 8:00 AM
3 trucks, 2 drivers
Truck can carry max 16 packages
Truck travel at 18 mph. 

ERRORS

status > 15:00:00

 File "/Users/eunice/github/package-delivery-ups/src/helper.py", line 47, in str_to_timedelta
    (hour, min, sec) = str.split(":")
ValueError: not enough values to unpack (expected 3, got 1)

--------------------------------------------------------------------

"""
