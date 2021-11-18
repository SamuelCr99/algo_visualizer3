from sorting_algo import draw_screen, check_quit
array_accesses = 0

def quick_sort(array,win):
    quick_sort_rec(array,0,len(array)-1,win)
    return

def quick_sort_rec(array,lo,hi,win):
    global array_accesses
    if lo >= hi:
        return array
    pivot = find_pivot(lo,hi) #Returns the pivot value based on our high and low. 
    array[lo],array[pivot] = array[pivot],array[lo]
    array_accesses += 2

    stop_lo = 0
    stop_hi = 0
    lower_pointer = 1
    upper_pointer = 0

    while(hi - upper_pointer >= lo + lower_pointer): #Following sequence partitions the array
        if(array[lo+lower_pointer] < array[lo]):
            array_accesses += 2
            lower_pointer += 1
        else:
            stop_lo = 1

        if(array[hi-upper_pointer] > array[lo]):
            array_accesses += 2
            upper_pointer += 1
        else:
            stop_hi = 1
        
        if (stop_lo and stop_hi):
            array[lo + lower_pointer],array[hi - upper_pointer] = array[hi - upper_pointer], array[lo + lower_pointer]
            array_accesses += 2
            draw_screen(win,array,array_accesses)
            check_quit()
            lower_pointer += 1
            upper_pointer += 1
            stop_lo = 0
            stop_hi = 0

    pivot = hi-upper_pointer
    array[lo],array[pivot] = array[pivot],array[lo]
    array_accesses += 2
    draw_screen(win,array,array_accesses)
    check_quit()

    array = quick_sort_rec(array,lo,pivot-1,win) #Sorts the lower of the two arrays
    array = quick_sort_rec(array,pivot+1,hi,win) #Sorts the upper

    return array
    

def find_pivot (lo,hi):
    return int((lo+hi)/2)
