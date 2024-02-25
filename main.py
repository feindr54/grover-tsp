import pennylane as qml
import numpy as np

# import other classes
from graph import Graph

# import other functions
from graph import generate_graph

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
def evaluate_wires(graph: Graph):
  cities = graph.nodes
  choice_bit_size = int(np.ceil(np.log2(cities)))

  cycle_wires = range(cities * choice_bit_size)

  all_wires = 10 # TODO - placeholder
  measured_wires = list(range(9)) # TODO - placeholder
  aux_wires = all_wires - 1 # in general, aux wire is usually the last wire
  return cycle_wires, measured_wires, aux_wires, all_wires

if __name__ == "__main__":
  NUM_CITIES = 5
  # TODO - randomly generate a graph, and send into circuit
  graph = generate_graph(NUM_CITIES)

  # evaluate wires function
  # returns measured_wires, aux_wire, total_wires
  cycle_wires, measured_wires, aux_wires, all_wires = evaluate_wires(graph)

  # create a device based number of wires
  dev = qml.device("default.qubit", wires=all_wires)

  # create a qnode that is depending on circuit and device
  circuit = qml.QNode(tsp_circuit, dev)

  # TODO - Generate a picture of the circuit

  # Generate the probabilities of the graph
  probs = circuit(graph)

  # generate a bar chart of the probabilities