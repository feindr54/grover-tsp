# Grover TSP
Recreating https://arxiv.org/abs/2212.02735 in Pennylane. We attempt to use Grover's Adaptive Search (GAS) to get an quicker solution to the Travelling Salesman Problem (TSP).

## Contents
1. [Background](#background)
1. [Basic Structure](#basic-structure)
2. [Oracle(s) implementation](#oracles-implementation)
3. [Problem Encoding](#problem-encoding)
4. [Cycle Length Comparing](#cycle-length-comparing)
5. [Hamiltonian Cycle Detection](#hamiltonian-cycle-detection)

## Background
The travelling salesman problem (TSP) determines a path in a graph that traverses through every node once, and returns to the starting point at the lowest cost/distance. This means that the algorithm is required to detect a Hamiltonian cycle in the graph, and to determine the cycle with the lowest total sum. As a result, TSP is an NP-hard problem, and the decision problem of TSP (for threshold $\leq k$) is NP-complete. TSP has many applications in (look for sectors), and it is desirable to reduce the runtime of the algorithm as much as possible.

Grover's Algorithm is an efficient database search algorithm developed in the 1990s, with its claim that the runtime is $O(\sqrt{N})$, where N represents the total number of states. Grover's algorithm consists of ...

Because Grovers only brings a quadratic speedup in runtime, the algorithm does not run in polynomial time. Nevertheless, any significant speedup is worth investigating.
## Basic Structure
TODO
## Problem Encoding
For an $N$-city TSP, there are at most $d\leq N-1$ choices for the salesman at each city. To encode the cities and the choices, we would require $Nm$ qubits, where $m = \lceil\log d\rceil$, which we refer as the Cycle Register $\ket{C}$.

Note: self edges and non-existing edges are represented by infinite costs.
## Oracle(s) implementation
The oracle is responsible for picking out a valid hamiltonian cycle that has the shortest total distance. Thus, 2 constraints come into play here - existence of hamiltonian cycle, and the cycle length/distance.

Here, 2 different oracles come into play. The cycle length comparing (CLC) oracle would be used to limit the length of the cycle.
## Cycle Length Comparing

Note: Update threshold from sampled results. Question: how to ensure $C_{th}$ is lower than all other suboptimal solution (without knowing the solution)?

Set precision of iQFT to 6.

## Hamiltonian Cycle Detection

## Testing
Generate $N$ data points in $[0,1]^2$ square, and edge weight is the Euclidean distance between nodes (2-norm).