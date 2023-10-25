from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for _ in range(self.array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        # Check if the key already exists in the linked list
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return

        # Key not found, insert the payload
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        list_at_index = self.array[array_index]

        # Check each item in the linked list
        for item in list_at_index:
            if item[0] == key:
                return item[1]

        # Key not found, return None
        return None

# Initialize your HashMap
blossom = HashMap(len(flower_definitions))

# Populate the HashMap with flower data
for flower in flower_definitions:
    blossom.assign(flower[0], flower[1])

# Retrieve the meaning of a flower
print(blossom.retrieve('daisy'))
print(blossom.retrieve('wisteria'))
print(blossom.retrieve('rose'))
