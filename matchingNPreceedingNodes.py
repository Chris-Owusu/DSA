def swap_nodes(input_list, val1, val2):
  node1 = input_list.head_node
  node2 = input_list.head_node
  node1_prev = None
  node2_prev = None

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()


#Updating the Preceding Nodes’ Pointers
# Still inside the swap_nodes() function
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2);

# Updating the Nodes’ Next Pointers
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node1.set_next_node(temp)
    
#Edge Cases

