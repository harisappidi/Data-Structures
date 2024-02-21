import sys
import time

def Coinchange_Rec(amount,coins,k):
    count = float('inf') # Considering positive infinity value as max default count
    if(amount<=0):      # returns 0 if considered coin combination will not give required value
        return 0
    for each_coin in range(0,k):
        if(coins[each_coin]<=amount):
            count = min(count,Coinchange_Rec(amount-coins[each_coin],coins,k)+1) #calling recursion to solve sub problems
    return count

if __name__ == "__main__":
    n =int(sys.argv[1]) #Takes the first argument which is amount value
    k = int(sys.argv[2]) #Takes the number of denominations value as second argument.
    d = []
    for i in range(3,k+3):
        d.append(int(sys.argv[i])) #Takes the denominations
    start_time = time.perf_counter_ns()
    Num_of_Coins_Used = Coinchange_Rec(n,d,k) #Initial call of naive recursive function
    print(Num_of_Coins_Used)
    print((time.perf_counter_ns()-start_time)) #Calculating execution time.