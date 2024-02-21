""" @author Harikrishna Sappidi (harikrishna.sappidi@gmail.com) """

comparison = 0                   #To count the number of comparisions

def merge3(a, p, m1, m2, r):
    global comparison
    left_arr = a[p-1 : m1]
    mid_arr = a[m1: m2 + 1]
    right_arr = a[m2 + 1 : r]

    left_arr.append(10000000)   #Using the value of greater than a million as infinity
    mid_arr.append(10000000)
    right_arr.append(10000000)
    left_index = 0
    mid_index = 0
    right_index = 0
    for i in range(p-1, r):
        min_value = min([left_arr[left_index], mid_arr[mid_index], right_arr[right_index]])   # finds the minimun value from the comparitive sub array's
        if min_value == left_arr[left_index]:
            a[i] = left_arr[left_index]
            left_index += 1
        elif min_value == mid_arr[mid_index]:
            a[i] = mid_arr[mid_index]
            mid_index += 1
        else:
            a[i] = right_arr[right_index]
            right_index += 1
        comparison+=2
    return a
    
# Merge_sort() function divides the array into sub arrays
def merge_sort3(a, p, r):
    if len(a[p-1:r])<=1:      # Handling Base Case
        return a
    else:
        m1 = p + ((r - p) // 3)      # MidIndex 1
        m2 = p + 2 * ((r-p) // 3)    # MidIndex 2

        merge_sort3(a, p, m1)          # Conquer
        merge_sort3(a, m1+1, m2 + 1)   # Conquer
        merge_sort3(a, m2+2, r)        # Conquer
        sorted_array = merge3(a, p, m1, m2, r)  # Merge
    return sorted_array

if __name__ == '__main__':
    from FileRead import DataList
    import time
    for arr in DataList:
        StartTime = time.monotonic()
        comparison = 0
        merged_list = merge_sort3(arr.copy(),1,len(arr))
        print(len(arr),',',comparison,',', '%.f'%((time.monotonic()- StartTime)*(10**3)))