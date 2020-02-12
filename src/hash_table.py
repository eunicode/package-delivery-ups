class HashTable:
    # Constructor. The default number of buckets is 10 (size).
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
    # Time complexity is O(N) bc we iterate the subcontainer list to check if the package has
    # already been inserted.
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
    # Time complexity is O(N) bc we iterate the subcontainer list to find the package
    def get(self, key):
        hash_value = self._hash_fxn(key)

        # Search bucket's subcontainer to find package matching the given ID
        for pkg_pair in self.bucket_list[hash_value]:
            if pkg_pair[0] == key:
                return pkg_pair[1]

    # ------------------------------------------------------------------
    # Method to update packages
    # Time complexity is O(N)
    def update(self, key, value):
        hash_value = self._hash_fxn(key)

        for pkg_pair in self.bucket_list[hash_value]:
            if pkg_pair[0] == key:
                pkg_pair[1] = value
                # print("hi")
                # print(pkg_pair[1])
        # print("update was run")
        # if self.bucket_list[key_hash] is not None:
        #     for pair in self.bucket_list[key_hash]:
        #         if pair[0] == key:
        #             pair[1] = value
        #             print(pair[1])
        #             # return True
        # else:
        #     print("There was an error with updating on key: " + key)

    # ------------------------------------------------------------------
    # Method to remove a package from the hash table
    # Time complexity is O(N)
    def delete(self, key):
        key_hash = self._hash_fxn(key)

        # if self.bucket_list[key_hash] is None:
        #     return False
        for i in range(0, len(self.bucket_list[key_hash])):
            if self.bucket_list[key_hash][i][0] == key:
                self.bucket_list[key_hash].pop(i)
                # return True
        # return False

    # ------------------------------------------------------------------
    # Print all packages
    # Time complexity = O(N^2)
    def print_values(self):
        my_str = f""
        for i in range(len(self.bucket_list)):
            for j in range(len(self.bucket_list[i])):
                my_str += f"\n{self.bucket_list[i][j]}"
        print(my_str)

    # ------------------------------------------------------------------
    # Print packages in specified bucket
    # Time complexity = O(N)
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

