import csv
from hash_table import HashTable

# Create hash table to hold all the package data
insert_into_hash_table = HashTable()
# Packages that must be delivered together
conjoined_pkgs = ["13", "14", "15", "16", "19", "20"]
first_truck = []
second_truck = []
third_truck = []

# Open csv file as a text file and get a file object
with open("csv/package_data.csv") as csv_file:
    # Pass file object (csv_file) to `reader` and get an iterable reader object
    # `csv_reader_pkg` takes O(N) space since its size is proportional to its input, the csv package data.
    csv_reader_pkg = csv.reader(csv_file, delimiter=",")
    # print_csv()

    # In a single pass, we add csv package data to our hash table, and load packages into trucks.
    # Time complexity is O(N^2) because of the for loop, and an implicit inner for loop
    # inside the outer for loop.
    # This for loop causes our hash table variable to take O(N) space because the data we add to the
    # hash table is proportional to the input, the csv package data.
    for row in csv_reader_pkg:
        # Copy csv package data into a dictionary.
        pkg_data = {
            "package_id": row[0],
            "location_id": "",
            "address": row[1],
            "city": row[2],
            "state": row[3],
            "zip": row[4],
            "deadline": row[5],
            "weight": row[6],
            "note": row[7],
            "delivery_start": "",
            "delivery_status": "At hub",
        }

        # Divide packages into trucks according to the restrictions.
        if pkg_data["note"] == "Can only be on truck 2":
            second_truck.append(pkg_data)
        if pkg_data["package_id"] in conjoined_pkgs:
            if pkg_data not in first_truck:
                first_truck.append(pkg_data)
        if "9:00" in pkg_data["deadline"]:
            if pkg_data not in first_truck:
                first_truck.append(pkg_data)
        if "10:30" in pkg_data["deadline"]:  # Todo: make more intelligent
            if pkg_data not in first_truck:
                first_truck.append(pkg_data)
        if "9:05" in pkg_data["note"]:
            second_truck.append(pkg_data)
        if "84104" in pkg_data["zip"]:
            if "10:30" not in pkg_data["deadline"]:
                third_truck.append(pkg_data)
        if "Wrong address" in pkg_data["note"]:
            pkg_data["address"] = "410 S State St"
            pkg_data["zip"] = "84111"
            third_truck.append(pkg_data)

        # Add remaining packages into trucks with the least number of packages
        if (
            pkg_data not in first_truck
            and pkg_data not in second_truck
            and pkg_data not in third_truck
        ):
            if len(second_truck) > len(third_truck):
                third_truck.append(pkg_data)
            else:
                second_truck.append(pkg_data)

        key = row[0]  # package ID
        value = pkg_data

        # Add values to hash table
        insert_into_hash_table.insert(key, value)

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
Find something better than if-statements to divide packages into trucks. 
A package can satisfy multiple if conditions.
"""
# -------------------------------------------------------------------
