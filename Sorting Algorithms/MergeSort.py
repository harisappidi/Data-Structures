""" @author Harikrishna Sappidi (harikrishna.sappidi@gmail.com) """

def Merge(arr,p,q,r):
    global comparison
    n1 = q-p+1
    n2 = r-q
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    for i in range(n1):
        L[i] = arr[p+i]
    for i in range(n2):
        R[i] = arr[q+i+1]
    L[n1] = 1000000000
    R[n2] = 1000000000
    i,j = 0,0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1            
        else:
            arr[k]=R[j]
            j+=1
        comparison+=1

def MergeSort(arr,p,r):
    if p<r:
        q = (p+r)//2
        MergeSort(arr,p,q)
        MergeSort(arr,q+1,r)
        Merge(arr,p,q,r)

comparison = 0

if __name__ == '__main__':
    from FileRead import DataList
    import time
    for arr in DataList:
        StartTime = time.monotonic()
        comparison = 0
        MergeSort(arr.copy(),0,len(arr)-1)
        print(len(arr),',', comparison,',', '%.f'%((time.monotonic()- StartTime)*(10**3)))
