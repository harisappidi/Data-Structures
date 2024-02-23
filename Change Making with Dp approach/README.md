# Coin Change Problem: Dynamic Programming Approach

## Overview
This project extends our exploration into the Coin Change problem by implementing and analyzing a Dynamic Programming (DP) approach. This method offers a more efficient solution compared to the Naïve Recursive and Greedy algorithms analyzed in Part A, especially in terms of time complexity and scalability.

## Problem Statement
The Coin Change problem seeks the minimum number of coins needed to make a given amount of change, using coins of specified denominations.

## Dynamic Programming Approach
- **Algorithm**: Utilizes a bottom-up approach to build a table `p[]` that stores the minimum number of coins required for amounts up to `n`, ensuring an optimal solution through subproblem optimization.
- **Complexity**: Achieves a time complexity of Θ(n*k), where `n` is the amount and `k` is the number of denominations, making it significantly more efficient than the recursive approach.

## Key Findings
- The DP approach consistently yields correct and optimal solutions across a variety of coin systems, including non-standard ("weird") systems.
- Outperforms the Naïve Recursive and Greedy algorithms in terms of efficiency, correctness, and applicability to diverse coin systems.

## Experimental Analysis
Experiments conducted on both standard and non-standard coin systems validate the effectiveness of the DP approach, highlighting its superior performance in achieving optimal solutions with reasonable computational resources.

## Conclusion
The Dynamic Programming approach is robust, versatile, and efficient for solving the Coin Change problem across different coin systems. It stands out as the recommended strategy for applications requiring precise and optimal change-making solutions, such as vending machines.

## How to Run
Make sure that Python source, of version greater than 3 has been installed on the machine using to run/test this project.

This project uses some of the standard python libraries installed with the Python source.

The folder consists of one batch file and 1 python file which is Dynamic Programming algorithm.

Make sure that the batch file and python file stay in same folder.

The program takes input as commandline arguments in the order of (a) an integer n representing the total change in cents, (b) number of denominations k, (c) k-size integer array d (i.e., d[1, 2, …, k]) that represents the denomination set. (All these integers are to be separated by a space)(Ex: python filename.py 11 4 1 5 10 25)

Double click on the chngmkDp.bat batch file to run the algorithm mentioned above in one shot (only works on Windows Operating System). The batch file works on the pre defined test data(given in canvas) and they can be viewed by editing the batch file or by running the batch files(in output console).

The python file is designed to run individually as well. To run the file individually on user defined input, commandline arguments should be passed as mentioned above.
For example: (Ex: python filename.py 11 4 1 5 10 25) 

The output format will be as follows for Dynamic programming Algorithm for Change-Making:
1) The first line will have a list of integers representing the coins used, and
2) The second line shows the time required to compute the solution in nanoseconds