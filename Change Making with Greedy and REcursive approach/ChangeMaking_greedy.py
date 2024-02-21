import time
import sys

def ChangeMaking_greedy(change,d,k):
    coins_used = []
    for i in range(0,k):
        if change//d[i] >= 1:
            coins_used.extend([d[i]]*(int(change/d[i])))          #appending valid coin values to the list
            change = change - (change//d[i]*d[i])     #reducing the input amount value by maximum number of current coin can be used 
    return coins_used

if __name__ == "__main__":
    n = int(sys.argv[1]) #Takes the first argument which is amount value
    k = int(sys.argv[2]) #Takes the number of denominations value as second argument.
    d = []
    for i in range(3,k+3):
        d.append(int(sys.argv[i])) #Takes the denominations
    d = [int(x/1) for x in d] #calculating the densities of denominations
    d.sort(reverse=True)    #Sorting the denominations in decreasing order
    start_time=time.perf_counter_ns()
    out = ChangeMaking_greedy(n,d,k)     #Calling greedy algorithm
    print(out)
    print((time.perf_counter_ns()-start_time))     #Calculating execution time.