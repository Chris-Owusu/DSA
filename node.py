# Create the Node class below:
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  # Define your get_value and get_link_node methods below:
  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node
  
  # Define your set_link_node method below:
  def set_link_node(self, link_node):
    self.link_node = link_node

    # Add your code below: Creating nodes
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

# Set the links
yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)

# Another Example
# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

my_node = Node(44)

print(my_node.get_value())