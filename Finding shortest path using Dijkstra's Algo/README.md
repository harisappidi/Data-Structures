# Experimental Analysis on Dijkstra’s Algorithm

## Overview
This project presents an experimental analysis of Dijkstra's Algorithm in finding the shortest path between two points, specifically applied to airport connections. The analysis covers the algorithm's performance across different sized datasets, emphasizing its practical applications and efficiency.

## Problem Statement
The focus is on leveraging Dijkstra’s Algorithm to efficiently determine the shortest path between a source and destination airport, using variously sized random graphs to simulate different network complexities.

## Methodology
- **Graph Generation**: Four random graphs were generated with increasing complexity, representing networks of airports connected by direct flight links. The sizes ranged from 25 nodes and 50 edges to 200 nodes and 3200 edges.
- **Analysis Metric**: The performance was measured by the time taken (in nano-seconds) to find the shortest path between randomly selected source and destination airports across the generated graphs.

## Results
A consistent increase in computation time was observed with the increase in graph size, validating the theoretical complexity of Dijkstra's Algorithm. The detailed experimental results are provided, showcasing the algorithm's scalability and performance across various network sizes.

## Conclusion
The experimental analysis confirms the theoretical efficiency of Dijkstra’s Algorithm in finding the shortest paths within graph-based data structures, proving its applicability in real-world scenarios such as routing and navigation systems.

## How to Run
Make sure that Python source, of version greater than 3 has been installed on the machine using to run/test this project.

This project uses some of the standard python libraries installed with the Python source.

The folder consists of a batch file and 1 python file which is Dijkstra's algorithm.

Make sure that the batch file and python file stay in same folder.

The input data has been given statically in the program, so no user input will be necessay. 
The test data is taken statically as per the instructions given in project description document.

Just run the batch file and it will give the output of 
1) shortest path between source airport and destination airport, and 
2) Time taken by the algorithm to run for each different sized input in nano seconds. separated by new line.

One can run the python file as well to get the output. You can edit the input values at the line number 48 to check for user defined input.