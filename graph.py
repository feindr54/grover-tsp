import numpy as np
import matplotlib.pyplot as plt

"""
Placeholder class to represent a graph
"""
class Graph:
  def __init__(self, nodes: int, coords, adj_matrix=None, adj_list=None):
    self.nodes = nodes
    self.coords = coords
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
def generate_graph(cities: int, choices: int) -> Graph:
  # TODO - finish the function, preferably to have about 20% of the adj_matrix to be 0
  # TODO -  generate N random points in [0,1]^2 space
  points = np.random.rand(cities, 2)

  # TODO - generate edges between random nodes
  adj_list = _sparse_graph(cities, d=choices)
  matrix = ...

  # matrix = np.random.uniform(-1,1, size=(cities, cities))
  # matrix = np.where(matrix >= 0, matrix, 100) * (np.ones_like(matrix) - np.eye(cities)) + (100*np.eye(cities))
  return Graph(nodes=cities, coords=points, adj_list=adj_list)

"""
Generate a random subset from a collection
"""
def _subset(cities: list[int], d: int):
  assert(d <= len(cities))

  edges = []
  for start in range(d):
    index = np.random.randint(start, len(cities))
    edges.append(cities[index])
    # swap cities with start
    temp = cities[start]
    cities[start] = cities[index]
    cities[index] = temp
  return edges

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
  adj_list = []
  for i in range(cities):
    edges = []
    for j in range(cities):
      if i != j: edges.append(j)
    edges = _subset(edges, d)
    adj_list.append(edges)
  return adj_list

"""
Displays the graph on a plot
"""
def plot_graph(g: Graph):
  for point in g.coords:
    plt.plot(point[0], point[1])
  for src in range(g.nodes):
    for dst in g.adj_list[src]:
      plt.plot([g.coords[src][0], g.coords[dst][0]], [g.coords[src][1], g.coords[dst][1]])
  plt.show()

if __name__ == "__main__":
  g: Graph = generate_graph(5, 3)
  print(g.adj_list)
  plot_graph(g)