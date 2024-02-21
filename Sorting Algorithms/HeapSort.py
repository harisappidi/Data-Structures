""" @author Harikrishna Sappidi (harikrishna.sappidi@gmail.com) """

comparison = 0

def heapify(arr,n,i):
    global comparison
    Max = i
    l = 2*i+1
    r = 2*i+2

    if l < n:
        comparison += 1
        if arr[i] < arr[l]:
            Max = l
    if r < n:
        comparison += 1
        if arr[Max] < arr[r]:
            Max = r

    if(Max != i):
        (arr[i],arr[Max])=(arr[Max],arr[i])
        heapify(arr,n,Max)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        (arr[i],arr[0])=(arr[0],arr[i])
        heapify(arr,i,0)

if __name__ == '__main__':
    from FileRead import DataList
    import time
    for arr in DataList:
        StartTime = time.monotonic()
        comparison = 0
        heap_sort(arr.copy())
        print(len(arr),',',comparison,',', '%.f'%((time.monotonic()- StartTime)*(10**3)))
