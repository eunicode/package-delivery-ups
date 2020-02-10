# Eunice Park ID: #001128345

from hash_table_instance import get_hash_map
from package_delivery import total_distance

# import datetime
from helper import interface_print
from helper import str_to_timedelta

# This is the display message that is shown when the user runs the program. The interface is accessible from here
print("Welcome to the package delivery system!\n")
# print("All packages were delivered in {} miles.".format(total_distance()))
print(f"All packages were delivered in {total_distance()} miles.")

# TEST
# test = get_hash_map().get("1")  # ["delivery_start"]
# print(test)

# -------------------------------------------------------------------
# Helper functions

# -------------------------------------------------------------------
while True:
    command = input(
        """
    =================================================================
    MENU:
    Enter "insert" to add a package.
    Enter "lookup" to lookup a package by its ID.
    Enter "status" to view the delivery status of all packages.
    Enter "exit" to exit program.
    =================================================================
    \nEnter a command:
    """
    )

    # Space-time complexity is O(N)
    # if user types 'timestamp' then they are prompted for a time to display.
    # Once a time is provided it will display all packages at that timestamp.
    # Runtime of this process is O(N)
    if command == "status":
        # try:
        package_status_time = input("Enter a time in the HH:MM:SS format: ")
        convert_input_time = str_to_timedelta(package_status_time)
        # (hour, min, sec) = package_status_time.split(":")
        # convert_user_time = datetime.timedelta(
        #     hours=int(hour), minutes=int(min), seconds=int(sec)
        # )

        # Space-time complexity is O(N^2)
        for count in range(1, 41):
            try:
                # first_time = get_hash_map().get(str(count))[9]
                first_time = get_hash_map().get(str(count))["delivery_start"]
                # second_time = get_hash_map().get(str(count))[10]
                second_time = get_hash_map().get(str(count))["delivery_status"]

                convert_first_time = str_to_timedelta(first_time)
                # (hour, min, sec) = first_time.split(":")
                # convert_first_time = datetime.timedelta(
                #     hours=int(hour), minutes=int(min), seconds=int(sec)
                # )
                convert_second_time = str_to_timedelta(second_time)
                # (hour, min, sec) = second_time.split(":")
                # convert_second_time = datetime.timedelta(
                #     hours=int(hour), minutes=int(min), seconds=int(sec)
                # )
            except ValueError:
                pass

            # First checks all packages against the given time determine if they have left the hub yet.
            if convert_first_time >= convert_input_time:
                # get_hash_map().get(str(count))[9] = "Leaves at " + first_time
                get_hash_map().get(str(count))["delivery_start"] = (
                    "Leaves at " + first_time
                )
                # get_hash_map().get(str(count))[10] = "At hub"
                get_hash_map().get(str(count))["delivery_status"] = "At hub"

                # filler
                interface_print(count)

            elif convert_first_time <= convert_input_time:
                # Then checks to see which packages have left the hub but have not been delivered yet
                if convert_input_time < convert_second_time:
                    # get_hash_map().get(str(count))[9] = "Left at " + first_time
                    get_hash_map().get(str(count))["delivery_start"] = (
                        "Left at " + first_time
                    )

                    # get_hash_map().get(str(count))[10] = "In transit"
                    get_hash_map().get(str(count))["delivery_status"] = "In transit"

                    # filler
                    interface_print(count)

                # Finally checks all packages that have already been delivered and displays the delivered time
                else:
                    # get_hash_map().get(str(count))[9] = "Left at " + first_time
                    get_hash_map().get(str(count))["delivery_start"] = (
                        "Left at " + first_time
                    )

                    # get_hash_map().get(str(count))[10] = "Delivered at " + second_time
                    get_hash_map().get(str(count))["delivery_status"] = (
                        "Delivered at " + second_time
                    )

                    # filler
                    interface_print(count)

        # except IndexError:
        #     print(IndexError)
        #     exit()
        # except ValueError:
        #     print("Invalid entry")
        #     exit()

    # -------------------------------------------------------------------
    # If 'lookup' is selected than the user is prompted for a package ID followed by a timestamp
    # Once that information is entered then the user will be shown a particular package at a given time
    elif command == "lookup":
        # try:
        count = input("Enter a package ID to lookup: ")
        first_time = get_hash_map().get(str(count))["delivery_start"]
        first_time = first_time.replace("Left at ", "")
        second_time = get_hash_map().get(str(count))["delivery_status"]
        second_time = second_time.replace("Delivered at", "")
        package_status_time = input("Enter a time in the HH:MM:SS format: ")

        convert_input_time = str_to_timedelta(package_status_time)
        # (h, m, s) = package_status_time.split(":")
        # convert_user_time = datetime.timedelta(
        #     hours=int(h), minutes=int(m), seconds=int(s)
        # )
        convert_first_time = str_to_timedelta(first_time)
        # (hr, min, sec) = first_time.split(":")
        # print(f"hr: {hr} min: {min} sec: {sec}")
        # convert_first_time = datetime.timedelta(
        #     hours=int(hr), minutes=int(min), seconds=int(sec)
        # )
        convert_second_time = str_to_timedelta(second_time)
        # (hour, minute, second) = second_time.split(":")
        # convert_second_time = datetime.timedelta(
        #     hours=int(hour), minutes=int(minute), seconds=int(second)
        # )

        # First checks if the package has left the hub yet
        if convert_first_time >= convert_input_time:

            get_hash_map().get(str(count))["delivery_status"] = "At hub"
            get_hash_map().get(str(count))["delivery_start"] = "Leaves at " + first_time

            # filler function
            interface_print(count)

        elif convert_first_time <= convert_input_time:
            # Then checks if the package has left the hub but has not been delivered yet
            if convert_input_time < convert_second_time:
                get_hash_map().get(str(count))["delivery_status"] = "In transit"
                get_hash_map().get(str(count))["delivery_start"] = (
                    "Left at " + first_time
                )

                # filler
                interface_print(count)

            # If the package has already been delivered than it displays the time
            else:
                get_hash_map().get(str(count))["delivery_status"] = (
                    "Delivered at " + second_time
                )

                get_hash_map().get(str(count))["delivery_start"] = (
                    "Left at " + first_time
                )

                # filler
                interface_print(count)
        # except ValueError:
        #     print("Invalid entry")
        #     exit()

    # -------------------------------------------------------------------
    elif command == "exit":
        exit()
    # -------------------------------------------------------------------
    else:
        print("Invalid entry")
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
Prevent "Left at" from printing twice
--------------------------------------------------------------------

"""
