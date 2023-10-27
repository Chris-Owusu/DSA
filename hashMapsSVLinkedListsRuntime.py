### Node

class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node
  
  def get_value(self):
    return self.value
  

### HashMaps

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return

### Linked List

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      string_list += str(current_node.value) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.next_node = next_node.get_next_node()
          current_node = None
        else:
          current_node = next_node

N = 6

#Insert Data Into HashMap
my_hashmap = HashMap(N)
my_hashmap.assign("Zachary", "Sunburn Sickness")
my_hashmap.assign("Elise", "Severe Nausea")
my_hashmap.assign("Mimi", "Stomach Flu")
my_hashmap.assign("Devan", "Malaria")
my_hashmap.assign("Gary", "Bacterial Meningitis")
my_hashmap.assign("Neeknaz", "Broken Cheekbone")

#Insert Data into LinkedList
my_linked_list = LinkedList(["Zachary", "Sunburn Sickness"])
my_linked_list.insert_beginning(["Elise", "Severe Nausea"])
my_linked_list.insert_beginning(["Mimi", "Stomach Flu"])
my_linked_list.insert_beginning(["Devan", "Malaria"])
my_linked_list.insert_beginning(["Gary", "Bacterial Meningitis"])
my_linked_list.insert_beginning(["Neeknaz", "Broken Cheekbone"])

#Get Zachary's Disease from a HashMap
hashmap_zachary_disease = my_hashmap.retrieve("Zachary") #Checkpoint 1
print("Zachary's disease is {0}".format(hashmap_zachary_disease))
hashmap_runtime = "1" #Checkpoint 2
print("The runtime of retrieving a value from a hashmap is O({0})\n\n".format(hashmap_runtime))


#Get Zachary's Disease from a Linked List
#Write Code here for Checkpoint 3
first = my_linked_list.get_head_node()
while first.get_value()[0] != "Zachary":
  first = first.get_next_node()

linked_list_zachary_disease = first.get_value()[1]
print("Zachary's disease is {0}".format(linked_list_zachary_disease))
linked_list_runtime = "N" #Checkpoint 4
print("The runtime of retrieving the first value added to a linked list is O({0})\n\n".format(linked_list_runtime))