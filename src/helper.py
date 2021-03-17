import re  # Regex
import datetime

from hash_table_instance import ht_pkgs

# -------------------------------------------------------------------
# Print package data - multiple line
def interface_print(count):
    my_str = f"""
    Package ID: {ht_pkgs.get(str(count))["package_id"]}
    Address: {ht_pkgs.get(str(count))["address"]} {ht_pkgs.get(str(count))["city"]} UT {ht_pkgs.get(str(count))["zip"]}
    Deadline: {ht_pkgs.get(str(count))["deadline"]}
    Package weight: {ht_pkgs.get(str(count))["weight"]}
    Truck status: {ht_pkgs.get(str(count))["delivery_start"]}
    Delivery status: {ht_pkgs.get(str(count))["delivery_status"]}"""

    print(my_str)


# -------------------------------------------------------------------
# Print package data - single line
def interface_print_single(count):
    my_str = f"""
    Package ID: {ht_pkgs.get(str(count))["package_id"]} | Address: {ht_pkgs.get(str(count))["address"]} {ht_pkgs.get(str(count))["city"]} UT {ht_pkgs.get(str(count))["zip"]} | Deadline: {ht_pkgs.get(str(count))["deadline"]} | Package weight: {ht_pkgs.get(str(count))["weight"]} | Truck status: {ht_pkgs.get(str(count))["delivery_start"]} | Delivery status: {ht_pkgs.get(str(count))["delivery_status"]}"""

    print(my_str)


# -------------------------------------------------------------------
# Print parsed csv data
def print_csv(reader_obj):
    line_count = 0

    for i in range(len(reader_obj)):
        my_str = f""  # Empty f-string

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

    # Multiple assignment
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

Formatted string literals, f-strings, are string literals that have an f at the beginning, 
and curly braces containing expressions that will be replaced with their values. 

You can use various types of quotation marks inside the expressions. 
Just make sure you are not using the same type of quotation mark on the outside of the f-string as you are using in the expression.
f"{'Eric Idle'}"
f'''Eric Idle'''

What is the Python equivalent of embedding an expression in a string? 
https://stackoverflow.com/questions/9763069/what-is-the-python-equivalent-of-embedding-an-expression-in-a-string-ie-ex

--------------------------------------------------------------------

"""
