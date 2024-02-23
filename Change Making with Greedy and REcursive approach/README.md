# Coin Change Problem: Recursive and Greedy Algorithms

## Overview
This project delves into solving the Coin Change problem, a classic example of dynamic programming and greedy algorithm application. We compare the performance of a Naïve Recursive approach and a Greedy algorithm to determine the minimum number of coins needed to make a given amount of change.

## Problem Statement
The Coin Change problem involves finding the fewest number of coins that you need to make up a given amount of money, given an unlimited supply of coins of given denominations.

## Algorithms
- **Naïve Recursive Approach**: Explores all combinations of coins that sum up to the target amount and selects the combination with the fewest coins.
- **Greedy Algorithm**: Selects the largest possible denominations first, moving to smaller ones, to reach the target amount.

## Experimental Analysis
We conducted experiments on different coin systems, including the US Coin System and a hypothetical "Weird Coin System", to analyze the efficiency and correctness of both algorithms.

## Key Findings
- The Naïve Recursive approach guarantees an optimal solution but is exponentially slow and resource-intensive.
- The Greedy algorithm is fast and efficient for certain coin systems (like the US Coin System) but does not always yield an optimal solution, especially for non-standard coin systems.

## Conclusion
Our analysis reveals that while the Greedy algorithm is efficient for standard coin systems, its application is limited by the coin system used. The Recursive approach, despite its correctness, may not be practical for large amounts due to its computational intensity. This project underscores the importance of algorithm selection based on the problem context and available resources.

## How to Run

Make sure that Python source, of version greater than 3 has been installed on the machine using to run/test this project.

This project uses some of the standard python libraries installed with the Python source.

The folder consists of two batch files and 2 python files which are naive recurvise algorithm and greedy algorithm.

Make sure both batch files and python files stay in same folder.

The programs take inputs as commandline arguments in the order of (a) an integer n representing the total change in cents, (b) number of denominations k, (c) k-size integer array d (i.e., d[1, 2, …, k]) that represents the denomination set. (All these integers are to be separated by a space)

Double click on the chngmkGreedy.bat and chngmkRecursive.bat batch files to run the algorithms mentioned above in one shot (only works on Windows Operating System). The batch files work on the pre defined test data(given in canvas) and they can be viewed by editing the batch file or by running the batch files(in output console).

Each python file is designed to run individually as well. To run these files individually on user defined input, commandline arguments should be passed as mentioned above.

The output format will be as follows for Greedy Algorithm for Change-Making:
1) The first line will have a list of integers representing the coins used, and
2) The second line shows the time required to compute the solution in nanoseconds

The output format will be as follows for Naive Recursive Algorithm for Change-Making:
1) The first line will have an integer representing the number of coins used, and
2) The second line shows the time required to compute the solution in nanoseconds