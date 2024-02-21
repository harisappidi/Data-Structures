""" @author Harikrishna Sappidi (harikrishna.sappidi@gmail.com) """

from FileRead import DataList
import time
import MergeSort as MS
import Three_Way_MergeSort as TMS
import InsertionSort as IS
import HeapSort as HS

if __name__ == '__main__':
    print("--------- Merge Sort Output ---------")
    for arr in DataList:
        StartTime = time.monotonic()
        MS.comparison = 0
        MS.MergeSort(arr.copy(),0,len(arr)-1)
        print(len(arr),',',MS.comparison,',', '%.f'%((time.monotonic()- StartTime)*(10**3)))
        
    print("--------- Three Way Merge Sort Output ---------")
    for arr in DataList:
        StartTime = time.monotonic()
        TMS.comparison = 0
        merged_list = TMS.merge_sort3(arr.copy(),1,len(arr))
        print(len(arr),',',TMS.comparison,',', '%.f'%((time.monotonic()- StartTime)*(10**3)))
       
    print("--------- Heap Sort Output ---------")
    for arr in DataList:
        StartTime = time.monotonic()
        HS.comparison = 0
        HS.heap_sort(arr.copy())
        print(len(arr),',',HS.comparison,',', '%.f'%((time.monotonic()- StartTime)*(10**3)))

    print("--------- Insertion Sort Output ---------")
    for arr in DataList:
        StartTime = time.monotonic()
        IS.comparison = 0
        IS.Insertion_Sort(arr.copy())
        print(len(arr),',',IS.comparison,',', '%.f'%((time.monotonic() - StartTime)*(10**3)))
