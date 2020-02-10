import csv
from hash_table import HashTable

# Calls the Hashmap class to create an object of Hashmap
insert_into_hash_table = HashTable()
first_truck = []  # list that represents the first truck delivery
# first_truck = []
second_truck = []  # list that represents the second truck delivery
third_truck = []  # list that represents the final truck delivery

# Open csv file as a text file and get a file object
with open("csv/package_data.csv") as csv_file:
    # Pass file object (csv_file) to `reader` and get an iterable reader object
    csv_reader = csv.reader(csv_file, delimiter=",")
    # print_csv()

    # Read in values from CSV file and insert them into key / value pairs
    # these values are what makes up the nested dictionary inside of the Hash table
    # Space-time complexity is O(N)
    for row in csv_reader:
        # package_ID_row_value = row[0]
        # address_row_value = row[1]
        # city_row_value = row[2]
        # state_row_value = row[3]
        # zip_row_value = row[4]
        # delivery_row_value = row[5]
        # size_row_value = row[6]
        # note_row_value = row[7]
        # delivery_start = ""
        # address_location = ""
        # delivery_status = "At hub"
        #
        package_data = {
            "package_id": row[0],  # 0
            "location_id": "",  # 1
            "address": row[1],  # 2
            "city": row[2],  # 3
            "state": row[3],  # 4
            "zip": row[4],  # 5
            "deadline": row[5],  # 6
            "weight": row[6],  # 7
            "note": row[7],  # 8
            "delivery_start": "",  # 9
            "delivery_status": "At hub",  # 10
        }

        # iterate_value = [
        #     package_ID_row_value,
        #     address_location,
        #     address_row_value,
        #     city_row_value,
        #     state_row_value,
        #     zip_row_value,
        #     delivery_row_value,
        #     size_row_value,
        #     note_row_value,
        #     delivery_start,
        #     delivery_status,
        # ]

        key = row[0]  # package ID
        value = package_data

        # In place constraints to create a list of packages that are loaded onto the trucks
        # The data structure here focuses on moving all attributes of a package into a nested list.
        # This allows for quick lookup and sorting that can be based on every package detail
        # Below is the set of constraints that determine which packages are loaded in either of the two trucks
        if value["deadline"] != "EOD":
            if "Must be delivered" in value["note"] or "None" in value["note"]:
                # this is a list that represents the first truck
                first_truck.append(value)
        if value["note"] == "Can only be on truck 2":
            second_truck.append(value)
        if "Delayed" in value["note"]:
            second_truck.append(value)
        # change the wrong address package to the correct address
        if "84104" in value["zip"] and "10:30" not in value["deadline"]:
            third_truck.append(value)
        if "Wrong address listed" in value["note"]:
            value["address"] = "410 S State St"
            value["zip"] = "84111"
            third_truck.append(value)

        if (
            value not in first_truck
            and value not in second_truck
            and value not in third_truck
        ):
            if len(second_truck) > len(third_truck):
                third_truck.append(value)
            else:
                second_truck.append(value)

        # adds all values in csv file to to a hash table
        insert_into_hash_table.insert(key, value)

    # function used to get the full list of values at start of day
    # Space-time complexity is O(1)
    # def get_hash_map():
    #     return insert_into_hash_table

    # function used to grab the packages that are loaded into the first truck
    # Space-time complexity is O(1)
    # def check_first_truck_first_trip():
    #     return first_truck

    # function used to grab the packages that are loaded into the second truck
    # Space-time complexity is O(1)
    # def check_second_truck_first_trip():
    #     return second_truck

    # function used to grab the packages that are loaded into the first truck last
    # Space-time complexity is O(1)
    # def check_first_truck_second_trip():
    #     return first_truck_second_trip


# =================================================================
# TEST

# Print package #1 details
# test_value = insert_into_hash_table.get("1")
# print(test_value)

# Print all packages
# insert_into_hash_table.print_values()

# Print packages in bucket 1
# insert_into_hash_table.print_bucket(1)

# print(f"map: {insert_into_hash_table.map}")

# -------------------------------------------------------------------
# See how packages are divided into trucks
# print(f"First truck = {first_truck}")
# print(f"Second truck = {second_truck}")
# print(f"First truck second trip = {third_truck}")


# def print_truck(truck):
#     my_str = f""
#     for package in truck:
#         my_str += f"{package['package_id']} ,"
#     print(my_str)


# print_truck(first_truck)
# print_truck(second_truck)
# print_truck(third_truck)


# =================================================================
#                             NOTES
# =================================================================
"""
Python "for" Loops (Definite Iteration)
https://realpython.com/python-for-loop/

--------------------------------------------------------------------
Reading and Writing CSV Files in Python
https://realpython.com/python-csv/

--------------------------------------------------------------------
TO DO

Avoid global variables

"""
# -------------------------------------------------------------------
