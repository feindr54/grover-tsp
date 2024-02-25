import pennylane as qml
import numpy as np

# import other classes
from graph import Graph

# import other functions

"""
Circuit responsible for the calculating the TSP
"""
def tsp_circuit(graph: Graph):
  # get the various types of the wires
  cycle_wires, _wires, all_wires = ...

  N = ...

  # iterate O(sqrt(N)) times
  for _ in range(N):
    # TODO - pass CLC oracle
    # TODO - pass HCD oracle
    pass

  # returns the probabilities of wires to be measured
  return qml.probs(measured_wires)

"""
Calculate the specific wires for each use (like a list)
Currently, return the encoded_wires, aux_wire, all_wires
"""
def evaluate_wires(graph):
  all_wires = 10 # TODO - placeholder
  measured_wires = list(range(9)) # TODO - placeholder
  aux_wires = all_wires - 1 # in general, aux wire is usually the last wire
  return measured_wires, aux_wires, all_wires

"""
Generates a random graph based on number of cities (vertices)
"""
def generate_graph(cities: int):
  # TODO - finish the function, preferably to have about 20% of the adj_matrix to be 0
  return [[],[]]

if __name__ == "__main__":
  NUM_CITIES = 5
  # TODO - randomly generate a graph, and send into circuit
  graph = generate_graph(NUM_CITIES)

  # evaluate wires function
  # returns measured_wires, aux_wire, total_wires
  measured_wires, aux_wires, all_wires = evaluate_wires(graph)

  # create a device based number of wires
  dev = qml.device("default.qubit", wires=all_wires)

  # create a qnode that is depending on circuit and device
  circuit = qml.QNode(tsp_circuit, dev)