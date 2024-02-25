"""
Placeholder class to represent a graph
"""
class Graph:
  def __init__(self, nodes: int, adj_matrix=None):
    self.nodes = nodes
    if adj_matrix is None:
      self.adj_matrix = [[0] * nodes for _ in range(nodes)]
    else:
      self.adj_matrix = adj_matrix

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
def generate_graph(cities: int) -> Graph:
  # TODO - finish the function, preferably to have about 20% of the adj_matrix to be 0
  return [[],[]]