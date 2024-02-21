import sys
import time

def Change_Dp(n, d, k):
    p = [0]     #list to store the minimum number of denominations needed to make at p[i] for i cents
    s = [0]     #list to store index of least possible denomination to provide change for i cents
    for i in range(1,n+1):
        count = float("inf")    #Considering positive infinity value as max default count
        for j in range(0,k):
            if d[j] <= i:
                if count > p[i-d[j]]+1:
                    count = p[i-d[j]]+1
                    coin_index = j
        p.append(count)
        s.append(coin_index)
    out = []
    while n>0:      #listing the minimum number of denominations used for given amount
        out.append(d[s[n]])
        n=n-d[s[n]]
    return out


if __name__ == "__main__":
    n =int(sys.argv[1]) #Takes the first argument which is amount value
    k = int(sys.argv[2]) #Takes the number of denominations value as second argument.
    d = []
    for i in range(3,k+3):
        d.append(int(sys.argv[i])) #Takes the denominations
    start_time = time.perf_counter_ns()
    out = Change_Dp(n,d,k) #Initial call of naive recursive function
    print(out)
    print((time.perf_counter_ns()-start_time)) #Calculating execution time.