class Graph:
  def __init__(self, nodes: int, adj_matrix=None):
    self.nodes = nodes
    if adj_matrix is None:
      self.adj_matrix = [[0] * nodes for _ in range(nodes)]
    else:
      self.adj_matrix = adj_matrix
  def add_edge(self, src: int, dst: int, cost: int):
    self.adj_matrix[src][dst] = cost