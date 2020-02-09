import re
import datetime

from hash_table_instance import get_hash_map


def interface_print(count):
    my_str = f"""
    Package ID: {get_hash_map().get(str(count))[0]}
    Address: {get_hash_map().get(str(count))[2]} {get_hash_map().get(str(count))[3]} UT {get_hash_map().get(str(count))[5]}
    Deadline: {get_hash_map().get(str(count))[6]}
    Package weight: {get_hash_map().get(str(count))[7]}
    Truck status: {get_hash_map().get(str(count))[9]}
    Delivery status: {get_hash_map().get(str(count))[10]}"""
    print(my_str)

    # print(
    #     """
    # ID: {}
    # Address: {} {} UT
    # Zipcode: {}
    # Deadline: {}
    # Weight: {}
    # Delivery Status: {}\
    # """
    # ).format(
    #     get_hash_map().get(str(count))[0],
    #     get_hash_map().get(str(count))[2],
    #     get_hash_map().get(str(count))[3],
    #     get_hash_map().get(str(count))[4],
    #     get_hash_map().get(str(count))[5],
    #     get_hash_map().get(str(count))[6],
    #     get_hash_map().get(str(count))[7],
    #     get_hash_map().get(str(count))[9],
    #     get_hash_map().get(str(count))[10],
    # )


# print(
#     "Package ID:",
#     get_hash_map().get(str(count))[0],
#     "   Street address:",
#     get_hash_map().get(str(count))[2],
#     get_hash_map().get(str(count))[3],
#     get_hash_map().get(str(count))[4],
#     get_hash_map().get(str(count))[5],
#     "  Required delivery time:",
#     get_hash_map().get(str(count))[6],
#     " Package weight:",
#     get_hash_map().get(str(count))[7],
#     "  Truck status:",
#     get_hash_map().get(str(count))[9],
#     "  Delivery status:",
#     get_hash_map().get(str(count))[10],
# )

# =================================================================
# Print parsed csv data
def print_csv(reader_obj):
    line_count = 0

    # for row in reader_obj:
    #     print(
    #         f"\tCol1: {row[0]} | Col2: {row[1]} | Col3: {row[2]} | Col4: {row[3]} | Col5: {row[4]} | Col6: {row[5]} | Col7: {row[6]} | Col8: {row[7]}"
    #     )
    #     line_count += 1
    for i in range(len(reader_obj)):
        my_str = f""
        for j in range(len(reader_obj[i])):
            my_str += f" || {reader_obj[i][j]}"
        print(my_str)
        line_count += 1

    print(f"Number of rows: {line_count}")


def str_to_timedelta(str):
    # Strip all characters that are not digits or `:`
    str = re.sub("[^0-9:]", "", str)
    (hour, min, sec) = str.split(":")
    return datetime.timedelta(hours=int(hour), minutes=int(min), seconds=int(sec))


# =================================================================


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

