def quick_sort(arr):
    return quick_sort_rec(arr,0,len(arr)-1)

def quick_sort_rec(arr,lo,hi):
    if lo >= hi:
        return arr
    pivot = find_pivot(lo,hi)
    arr[lo],arr[pivot] = arr[pivot],arr[lo]

    stop_lo = 0
    stop_hi = 0
    lower_pointer = 1
    upper_pointer = 0

    while(hi - upper_pointer > lo + lower_pointer):
        if(arr[lo+lower_pointer] < arr[lo]):
            lower_pointer += 1
        else:
            stop_lo = 1

        if(arr[hi-upper_pointer] > arr[lo]):
            upper_pointer += 1
        else:
            stop_hi = 1
        
        if (stop_lo and stop_hi):
            arr[lo + lower_pointer],arr[hi - upper_pointer] = arr[hi - upper_pointer], arr[lo + lower_pointer]
            lower_pointer += 1
            upper_pointer += 1
            stop_lo = 0
            stop_hi = 0
    pivot = lo+lower_pointer
    arr[lo],arr[pivot] = arr[pivot],arr[lo]

    arr = quick_sort_rec(arr,lo,pivot-1)
    arr = quick_sort_rec(arr,pivot+1,hi)

    return arr
    

def find_pivot (lo,hi):
    return int((hi+lo)/2)

test = [1,3,5,9,8,7,6]


print(quick_sort(test))
