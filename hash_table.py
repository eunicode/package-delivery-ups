# class HashTableEntry:
#     def __init__(self, key, item):
#         self.key = key
#         self.item = item


class HashTable:
    """
    Hash table
    put()
    get()
    remove()
    update()
    """

    # Constructor
    # Time complexity is O(N)
    def __init__(self, initial_capacity=10):
        # Chaining: initialize slots with empty lists
        self.map = []
        for elm in range(initial_capacity):
            self.map.append([])

    # private getter to create a hash key / Function to be used internally by the class
    # Space complexity is O(1)
    # Time complexity is
    def _get_hash(self, key):
        return int(key) % len(self.map)
        # return bucket

    # Insert a new package value into the hash table
    # Space complexity is O(N)
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Space-time complexity is O(N)
    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print("There was an error with updating on key: " + key)

    # Grab a value from the hash table
    # Space-time complexity is O(N)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Remove a value from the hash table
    # runtime is O(N)

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False


# =================================================================
# TEST

ht = HashTable()

ht.insert(
    1,
    [1, "195 W Oakland Ave", "Salt Lake City", "UT", "84115", "10:30:00", "21", "None"],
)

# print(f"map: {ht.map}")

# for key in (1, 2):
#     v = ht.get(key)
#     print(v)

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
RANDOM

Looking up a key that does not exist returns `None`.

bucket array

put() / get() / remove()
--------------------------------------------------------------------
"""
# ------------------------------------------------------------------

