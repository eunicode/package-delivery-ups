import re  # Regex
import datetime

from hash_table_instance import insert_into_hash_table

# -------------------------------------------------------------------
# Print package data - multiple line
def interface_print(count):
    my_str = f"""
    Package ID: {insert_into_hash_table.get(str(count))["package_id"]}
    Address: {insert_into_hash_table.get(str(count))["address"]} {insert_into_hash_table.get(str(count))["city"]} UT {insert_into_hash_table.get(str(count))["zip"]}
    Deadline: {insert_into_hash_table.get(str(count))["deadline"]}
    Package weight: {insert_into_hash_table.get(str(count))["weight"]}
    Truck status: {insert_into_hash_table.get(str(count))["delivery_start"]}
    Delivery status: {insert_into_hash_table.get(str(count))["delivery_status"]}"""
    print(my_str)


# -------------------------------------------------------------------
# Print package data - single line
def interface_print_single(count):
    my_str = f"""
    Package ID: {insert_into_hash_table.get(str(count))["package_id"]} | Address: {insert_into_hash_table.get(str(count))["address"]} {insert_into_hash_table.get(str(count))["city"]} UT {insert_into_hash_table.get(str(count))["zip"]} | Deadline: {insert_into_hash_table.get(str(count))["deadline"]} | Package weight: {insert_into_hash_table.get(str(count))["weight"]} | Truck status: {insert_into_hash_table.get(str(count))["delivery_start"]} | Delivery status: {insert_into_hash_table.get(str(count))["delivery_status"]}"""
    print(my_str)


# -------------------------------------------------------------------
# Print parsed csv data
def print_csv(reader_obj):
    line_count = 0

    for i in range(len(reader_obj)):
        my_str = f""
        for j in range(len(reader_obj[i])):
            my_str += f" || {reader_obj[i][j]}"
        print(my_str)
        line_count += 1

    print(f"Number of rows: {line_count}")


# -------------------------------------------------------------------
# Convert string to timedelta
def str_to_timedelta(str):
    # Strip all characters that are not digits or `:`
    str = re.sub("[^0-9:]", "", str)
    (hour, min, sec) = str.split(":")
    return datetime.timedelta(hours=int(hour), minutes=int(min), seconds=int(sec))


# =================================================================
#                             NOTES
# =================================================================
"""
Python String Formatting Best Practices
https://realpython.com/python-string-formatting/

Python 3's f-Strings: An Improved String Formatting Syntax (Guide)
https://realpython.com/python-f-strings/

What is the Python equivalent of embedding an expression in a string? 
https://stackoverflow.com/questions/9763069/what-is-the-python-equivalent-of-embedding-an-expression-in-a-string-ie-ex

--------------------------------------------------------------------

"""

