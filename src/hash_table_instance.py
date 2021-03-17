import csv
from hash_table import HashTable

# Create hash table to hold all the packages and data
ht_pkgs = HashTable()
# Packages that must be delivered together
conjoined_pkgs = ["13", "14", "15", "16", "19", "20"]
# Variables to hold packages loaded into trucks
truck1 = []
truck2 = []
truck3 = []

# Open csv file as a text file and get a file object
with open("csv/package_data.csv") as csv_file:
    # Pass file object (csv_file) to `reader` and get an iterable reader object
    # `csv_reader_pkg` takes O(N) space since its size is proportional to its input, the csv package data.
    csv_reader_pkg = csv.reader(csv_file, delimiter=",")
    # print_csv()

    # In a single pass, we add load packages into trucks and add csv package data to our hash table.
    # Time complexity is O(N^2) because of the for loop, and an implicit inner for loop inside the
    # outer for loop.
    # This for loop causes our hash table variable `ht_pkgs` to take O(N) space because the data we
    # add to the hash table is proportional to the input, the csv package data.
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
            truck2.append(pkg_data)
        if pkg_data["package_id"] in conjoined_pkgs:
            if pkg_data not in truck1:
                truck1.append(pkg_data)
        if "9:00" in pkg_data["deadline"]:
            if pkg_data not in truck1:
                truck1.append(pkg_data)
        if "10:30" in pkg_data["deadline"]:  # Todo: make more intelligent
            if pkg_data not in truck1:
                truck1.append(pkg_data)
        if "9:05" in pkg_data["note"]:
            truck2.append(pkg_data)
        if "84104" in pkg_data["zip"]:
            if "10:30" not in pkg_data["deadline"]:
                truck3.append(pkg_data)
        if "Wrong address" in pkg_data["note"]:
            pkg_data["address"] = "410 S State St"
            pkg_data["zip"] = "84111"
            truck3.append(pkg_data)

        # Add remaining packages into trucks with the least number of packages
        if pkg_data not in truck1 and pkg_data not in truck2 and pkg_data not in truck3:
            if len(truck2) > len(truck3):
                truck3.append(pkg_data)
            else:
                truck2.append(pkg_data)

        key = row[0]  # package ID
        value = pkg_data

        # Add values to hash table
        ht_pkgs.insert(key, value)

# =================================================================
# TEST

# Print package #1 details
# test_value = ht_pkgs.get("1")
# print(test_value)

# Print all packages
# ht_pkgs.print_values()

# Print packages in bucket 1
# ht_pkgs.print_bucket(1)

# print(f"bucket_list: {ht_pkgs.bucket_list}")

# -------------------------------------------------------------------
# See how packages are divided into trucks
# print(f"First truck = {truck1}")
# print(f"Second truck = {truck2}")
# print(f"First truck second trip = {truck3}")

# def print_truck(truck):
#     my_str = f""
#     for package in truck:
#         my_str += f"{package['package_id']} ,"
#     print(my_str)

# print_truck(truck1)
# print_truck(truck2)
# print_truck(truck3)


# =================================================================
#                             NOTES
# =================================================================
"""
WHAT HASH TABLE LOOKS LIKE
{
    # Bucket #1
    [ 
        ["1",["1","195 W Oakland Ave",], # one package 
        ...3 more arrays
    ], 
    ...9 more arrays
}

--------------------------------------------------------------------
WHAT TRUCK1 LOOKS LIKE
[ 
    { package_id: '1;, address: 'some-string', weight: '9'}, 
    ...
]

--------------------------------------------------------------------
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
