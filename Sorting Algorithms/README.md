# Data Structures: Sorting Algorithms Analysis

## Overview
This project explores the practical performance of various sorting algorithms, including Merge Sort, Three-Way Merge Sort, Heap Sort, and Insertion Sort. Through experimental analysis, we investigate the efficiency of these algorithms in terms of the number of comparisons and execution time across different data sets.

## Algorithms Analyzed
- **Merge Sort**: A divide-and-conquer algorithm that divides the input array into two halves, sorts the halves, and then merges them.
- **Three-Way Merge Sort**: Similar to Merge Sort but divides the input array into three parts, potentially improving efficiency on certain data sets.
- **Heap Sort**: Utilizes the heap data structure to sort elements, offering a good balance between time complexity and space usage.
- **Insertion Sort**: A simple comparison-based sorting technique, efficient for small data sets or nearly sorted arrays.

## Experimental Setup
The analysis was conducted using Python 3.10 on a system equipped with 16GB RAM, Windows 11 Pro, and an 11th Gen i7 processor. Sorting algorithms were tested against data sets of varying sizes and orders (ascending, descending, random, and identical) to assess their performance under different conditions.

## Results
Our findings illustrate the trade-offs between algorithm complexity, execution time, and memory usage. Notably:
- Insertion Sort performs exceptionally well on nearly sorted or small datasets.
- Merge Sort and Three-Way Merge Sort are efficient for large datasets but require additional memory.
- Heap Sort offers a balanced solution, being relatively efficient without needing extra space.

## Conclusion
The project highlights the importance of selecting the appropriate sorting algorithm based on the characteristics of the data set and the constraints of the computational environment. Further exploration into different programming languages and system configurations may offer additional insights into the performance of these algorithms.

## How to Run
Instructions for setting up and running the analysis are provided below, allowing others to replicate the study or explore the performance of the algorithms with different data sets.


-> Make sure that Python source, of version greater than 3 has been installed on the machine using to run/test this project.

-> Make sure the following python libraries are available in the Python source:
os,
time,
glob.

-> The folder consists of one batch file, 6 python files, and a folder named "Files" which contains the 20 different input datasets. These are the necessary things to use this project.

-> If you would like to test on your own dataset files, kindly replace the existing files in the folder "Files" with your files. Each file will have numbers seperated by a new line. Those files contain random numbers, identical numbers, ascending and descending ordered of sizes 20,000, 40,000, 80,000, 160,000, and 320,000.
- random data
- sorted random data
- reverse (descending) sorted random data
- all identical data


-> Double click on the _Auto run Programs.bat_ batch file to run all the algorithms mentioned above in one shot (only works on Windows Operating System).

-> Each python file is designed to run individually as well. Open the particular python file in any Python Integrated Development Enviroments and run it.

-> Each python file will give output by using the algorithm as file name represents.

-> Note that FileRead.py is being imported in all the python files which reads the data present in 20 datasets present in "Files" folder.

-> Output will be in the order of "Number of elements in the file, Number of Comparisons made, and Time taken to sort the each file data in Milli Seconds", separated by commas.