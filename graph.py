import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

"""
Placeholder class to represent a graph
"""
class Graph:
  def __init__(self, nodes: int, coords, adj_matrix=None, adj_list=None):
    self.nodes = nodes
    self.coords = np.array(coords)
    if adj_matrix is None:
      self.adj_matrix = [[0] * nodes for _ in range(nodes)]
    else:
      self.adj_matrix = adj_matrix
    self.adj_list = adj_list

  def _adj_list_from_matrix(self):
    self.adj_list = []
    for i in range(len(self.adj_matrix)):
      row = self.adj_matrix[i]
      r = []
      for dst in range(self.nodes):
        r.append((dst, row[dst]))
      self.adj_list.append(r)

  def add_edge(self, src: int, dst: int, cost: int):
    self.adj_matrix[src][dst] = cost

"""
Generates a random graph based on number of cities (vertices)
"""
def generate_graph(cities: int, choices: int, is_complete: bool=False) -> Graph:
  if not is_complete: assert((cities % 2 == 0) or (choices % 2 == 0)), "Product of nodes and degrees must be even"
  # TODO - finish the function, preferably to have about 20% of the adj_matrix to be 0
  # generate N random points in [0,1]^2 space
  points = np.random.rand(cities, 2)

  # generate edges between random nodes
  if is_complete or (choices == cities-1):
    adj_list = _complete_graph(cities)
  else:
    adj_list = _sparse_graph(cities, d=choices)

  return Graph(nodes=cities, coords=points, adj_list=adj_list)

"""
Generate a full complete graph for n cities
"""
def _complete_graph(cities: int):
  adj_list = []
  for i in range(cities):
    edges = []
    for j in range(cities):
      if i != j: edges.append(j)
    adj_list.append(edges)
  return adj_list

"""
Generate sparse d-complete graph for n cities
"""
def _sparse_graph(cities: int, d: int):
  dummy=True
  while dummy:
    dummy = False
    adj_list = [[] for _ in range(cities)]
    choices = [[y for y in range(cities) if x != y] for x in range(cities)]
    indices = [0] * cities
    endings = [cities-2] * cities
    for src in range(cities):
      while (len(adj_list[src]) < d):
        # attempt to add a new edge
        if indices[src] == endings[src]:
          dummy = True
          break
        remaining_choices = choices[src][indices[src]:endings[src]+1]
        # if (len(remaining_choices) < 1):
        #   dummy = True
        #   break
        new_choice = np.random.choice(remaining_choices)
        if (len(adj_list[new_choice]) >= d):
          _swap(choices[src], choices[src].index(new_choice), endings[src])
          endings[src] -= 1
        else:
          _swap(choices[src], choices[src].index(new_choice), indices[src])
          _swap(choices[new_choice], choices[new_choice].index(src), indices[new_choice])
          adj_list[src].append(new_choice)
          adj_list[new_choice].append(src)
          indices[src] += 1
          indices[new_choice] += 1
      # print(adj_list)
      if dummy: break

  return adj_list

def _swap(arr, old, new):
  temp = arr[old]
  arr[old] = arr[new]
  arr[new] = temp

"""
Displays the graph on a plot
"""
def plot_graph(g: Graph):
  # for point in g.coords:
  #   plt.plot(point[0], point[1])
  plt.scatter(x=g.coords[:,0], y=g.coords[:,1])
  for src in range(g.nodes):
    for dst in g.adj_list[src]:
      plt.plot([g.coords[src,0], g.coords[dst,0]], [g.coords[src,1], g.coords[dst,1]])
  plt.show()

if __name__ == "__main__":
  g: Graph = generate_graph(8, 3)
  print(g.adj_list)
  plot_graph(g)