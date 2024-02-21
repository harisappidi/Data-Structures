""" @author Harikrishna Sappidi (harikrishna.sappidi@gmail.com) """

comparison = 0
def Insertion_Sort(l):
    length = len(l)
    global comparison
    for i in range(1,length):
        key = l[i]
        j = i-1
        while  j>=0 and l[j] > key:
                l[j+1] = l[j]
                j -= 1
        if j>=0:
            comparison += i-j
        else:
            comparison += i
        l[j+1] = key
if __name__ == '__main__':
    from FileRead import DataList
    import time
    for arr in DataList:
        StartTime = time.monotonic()
        comparison = 0
        Insertion_Sort(arr.copy())
        print(len(arr),',',comparison,',', '%.f'%((time.monotonic() - StartTime)*(10**3)))
