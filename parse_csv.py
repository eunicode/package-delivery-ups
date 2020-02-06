import csv
from hash_table import HashTable

# Print parsed csv data
def print_csv():
    line_count = 0

    for row in csv_reader:
        print(
            f"\tCol1: {row[0]} | Col2: {row[1]} | Col3: {row[2]} | Col4: {row[3]} | Col5: {row[4]} | Col6: {row[5]} | Col7: {row[6]} | Col8: {row[7]}"
        )
        line_count += 1

    print(f"Processed {line_count} lines.")


# Open csv file as a text file and get a file object
with open("package_data.csv") as csv_file:
    # Pass file object (csv_file) to `reader` and get an iterable reader object
    csv_reader = csv.reader(csv_file, delimiter=",")
    # print_csv()

    # Calls the Hashmap class to create an object of Hashmap
    insert_into_hash_table = HashTable()
    first_truck = []  # list that represents the first truck delivery
    second_truck = []  # list that represents the second truck delivery
    first_truck_second_trip = []  # list that represents the final truck delivery

    # Read in values from CSV file and insert them into key / value pairs
    # these values are what makes up the nested dictionary inside of the Hash table
    # Space-time complexity is O(N)
    for row in csv_reader:
        package_ID_row_value = row[0]
        address_row_value = row[1]
        city_row_value = row[2]
        state_row_value = row[3]
        zip_row_value = row[4]
        delivery_row_value = row[5]
        size_row_value = row[6]
        note_row_value = row[7]
        delivery_start = ""
        address_location = ""
        delivery_status = "At hub"
        iterate_value = [
            package_ID_row_value,
            address_location,
            address_row_value,
            city_row_value,
            state_row_value,
            zip_row_value,
            delivery_row_value,
            size_row_value,
            note_row_value,
            delivery_start,
            delivery_status,
        ]

        key = package_ID_row_value
        value = iterate_value

        # In place constraints to create a list of packages that are loaded onto the trucks
        # The data structure here focuses on moving all attributes of a package into a nested listed.
        # This allows for quick lookup and sorting that can be based on every package detail
        # Below is the set of constraints that determine which packages are loaded in either of the two trucks
        if value[6] != "EOD":
            if "Must" in value[8] or "None" in value[8]:
                # this is a list that represents the first truck
                first_truck.append(value)
        if "Can only be" in value[8]:
            second_truck.append(value)
        if "Delayed" in value[8]:
            second_truck.append(value)
        # change the wrong address package to the correct address
        if "84104" in value[5] and "10:30" not in value[6]:
            first_truck_second_trip.append(value)
        if "Wrong address listed" in value[8]:
            value[2] = "410 S State St"
            value[5] = "84111"
            first_truck_second_trip.append(value)
        if (
            value not in first_truck
            and value not in second_truck
            and value not in first_truck_second_trip
        ):
            if len(second_truck) > len(first_truck_second_trip):
                first_truck_second_trip.append(value)
            else:
                second_truck.append(value)
        # adds all values in csv file to to a hash table
        insert_into_hash_table.insert(key, value)

    # function used to get the full list of values at start of day
    # Space-time complexity is O(1)
    def get_hash_map():
        return insert_into_hash_table

    # function used to grab the packages that are loaded into the first truck
    # Space-time complexity is O(1)
    def check_first_truck_first_trip():
        return first_truck

    # function used to grab the packages that are loaded into the second truck
    # Space-time complexity is O(1)
    def check_second_truck_first_trip():
        return second_truck

    # function used to grab the packages that are loaded into the first truck last
    # Space-time complexity is O(1)
    def check_first_truck_second_trip():
        return first_truck_second_trip

    # TEST
    # for key in (1, 2):
    #     v = insert_into_hash_table.get(key)
    #     print(v)

    # vs = insert_into_hash_table.get(1)
    # print(vs)

# =================================================================
# TEST

# for key in range(1):
#     v = insert_into_hash_table.get(key)
#     print(v)

# =================================================================
#                             NOTES
# =================================================================
"""
Python "for" Loops (Definite Iteration)
https://realpython.com/python-for-loop/

--------------------------------------------------------------------
Reading and Writing CSV Files in Python
https://realpython.com/python-csv/


"""
