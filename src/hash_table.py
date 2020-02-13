class HashTable:
    # Constructor. The default number of buckets is 10 (size).
    # Time complexity = O(N), where N is `size`
    def __init__(self, size=10):
        self.size = size
        self.bucket_list = []
        # Chaining: Add an empty list (subcontainer) to every bucket.
        # Chaining means a bucket/index holds a list instead of a single value
        for bucket in range(size):
            self.bucket_list.append([])

    # ------------------------------------------------------------------
    # Hash function that is used internally by the class.
    # Returns the bucket/slot the package is in.
    # Time complexity = O(1)
    def _hash_fxn(self, key):
        return int(key) % self.size

    # ------------------------------------------------------------------
    # Method to add/put packages in the hash table.
    # The worst case time complexity is O(N) bc all the packages could be added to the same bucket.
    # However, this will not happen bc our package IDs are sequential, not random.
    # Therefore our packages will be evenly distributed.
    # The number of packages in each bucket can be calculated as N/size.
    # In this case, we will always have 4 packages per bucket, 40/10 (x % 10, where x is 1-40).
    # However, we can adjust the hash function and number of buckets so that the number of packages
    # in each bucket remains small.
    # Therefore the number of packages in each bucket can be independent of the input.
    # So 4 can be treated as a constant, and our average time complexity can be simplified to O(1)
    def insert(self, key, value):
        # Determine which bucket the package will go into
        pkg_hash_value = self._hash_fxn(key)
        pkg_pair = [key, value]  # package ID and data

        # Check if package has already been inserted
        for package_pair in self.bucket_list[pkg_hash_value]:
            if package_pair[0] == key:
                assert False, "This package has already been inserted!"
                return

        # Insert package
        self.bucket_list[pkg_hash_value].append(pkg_pair)

    # ------------------------------------------------------------------
    # Method to get package data from hash table
    # Average time complexity is O(1) bc our hash function evenly distributes packages into small
    # bucket lists.
    # The worst case time complexity is O(N), but this will not happen bc our hash function
    # evenly distributes packages into buckets, and we can adjust the hash function and hash table
    # size so that our buckets will always have a small number of packages.
    def get(self, key):
        hash_value = self._hash_fxn(key)

        # Search bucket's subcontainer to find package matching the given ID
        for pkg_pair in self.bucket_list[hash_value]:
            if pkg_pair[0] == key:
                return pkg_pair[1]

    # ------------------------------------------------------------------
    # Method to update packages
    # Average time complexity is O(1) bc our hash function evenly distributes packages into small
    # bucket lists (constant size).
    def update(self, key, value):
        hash_value = self._hash_fxn(key)

        # Search for package ID in bucket's subcontainer
        for i, pkg_pair in enumerate(self.bucket_list[hash_value]):
            if pkg_pair[0] == key:
                pkg_pair[1] = value
                break
            # If we can't find the package ID in bucket, the package doesn't exist
            if i == len(self.bucket_list[hash_value]) - 1 and pkg_pair[0] != key:
                assert False, "Package does not exist!"

    # ------------------------------------------------------------------
    # Method to remove a package from the hash table
    # Average time complexity is O(1) bc our hash function evenly distributes packages into small
    # bucket lists (constant size).
    def remove(self, key):
        key_hash = self._hash_fxn(key)

        # Search for package ID in bucket's subcontainer, delete package if found
        for i in range(0, len(self.bucket_list[key_hash])):
            if self.bucket_list[key_hash][i][0] == key:
                self.bucket_list[key_hash].pop(i)

    # ------------------------------------------------------------------
    # Print all packages
    # Time complexity is O(N * 1)
    # The outer for loop is O(N) bc we will iterate through all the packages in the hash table.
    # The inner for loop is O(1) bc the bucket subcontainer will always carry a small number of
    # packages that is independent of the input.
    def print_values(self):
        my_str = f""
        for i in range(len(self.bucket_list)):
            for j in range(len(self.bucket_list[i])):
                my_str += f"\n{self.bucket_list[i][j]}"
        print(my_str)

    # ------------------------------------------------------------------
    # Print packages in specified bucket
    # Average time complexity is O(1) bc our hash function evenly distributes packages into buckets.
    # Therefore, our bucket will always have a small number of packages, a constant which is not
    # proportional to the size of the input (number of packages).
    def print_bucket(self, bucket):
        my_str = f""
        for i in range(len(self.bucket_list[bucket])):
            my_str += f"\n{self.bucket_list[bucket][i]}"
        print(my_str)


# =================================================================
# TEST

# ht = HashTable()

# ht.insert(
#     "1",
#     [
#         "1",
#         "195 W Oakland Ave",
#         "Salt Lake City",
#         "UT",
#         "84115",
#         "10:30:00",
#         "21",
#         "None",
#     ],
# )

# ht.insert(
#     "2", ["2", "2530 S 500 E", "Salt Lake City", "UT", "84106", "EOD", "44", "None"]
# )

# print(f"bucket_list: {ht.bucket_list}")

# for key in ("1", "2"):
#     value = ht.get(key)
#     print(value)

# =================================================================
#                             NOTES
# =================================================================
"""
TUPLES

--------------------------------------------------------------------
COLLISION 

Keys that return the same hash value by our hashing function = collision

--------------------------------------------------------------------
COLLISION RESOLUTION: SEPARATE CHAINING

In chaining, the slots in the hash table are initialized with empty lists
Chaining then avoids conflict by allowing multiple elements to have the same hash value. 
It also avoids the problem of insertions as the load factor increases, since we don't have to look for a slot. 
Moreover, the hash table can hold more values than the number of available slots, since each slot holds a list that can grow.

Of course, if a particular slot has many items, searching them can get very slow, since we have to do a linear search through the list until we find the element that has the key we want. 
This can slow down retrieval (linear search through list items until we find a match). 
Alternative: self-balancing BSTs instead of lists.

Alternative: open addressing e.g. linear probing aka open-addressing hashing

--------------------------------------------------------------------
ASSERT
https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python

--------------------------------------------------------------------
RANDOM

Looking up a key that does not exist returns `None`.

bucket_list = bucket array = table
a bucket/slot/index holds a subcontainer, a list
Possible semantics confusion: bucket can refer to the index, or to the value of the index, 
the subcontainer list
Correct term is hash value

[ 0, 1, 2 ]
[ [], [], [] ]
put() / get() / remove()
--------------------------------------------------------------------
"""
# ------------------------------------------------------------------

