# Bring in the Vertex class from vertex.py
from vertex import Vertex

# Define Graph below...
class Graph:
  def __init__(self, directed=False):
    self.directed = directed 
    self.graph_dict = {}

  def add_vertex(self, vertex):
    print("Adding " + vertex.value)
    self.graph_dict[vertex.value] = vertex


grand_central = Vertex("Grand Central Station")

# Uncomment this code after you've defined Graph
railway = Graph()

# Uncomment these lines after you've completed .add_vertex()
print(railway.graph_dict)
railway.add_vertex(grand_central)
print(railway.graph_dict)
