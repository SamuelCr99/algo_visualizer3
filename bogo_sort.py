import random
from sorting_algo import draw_screen, check_quit

array_accesses = 0

def check_sorted(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True


def bogo_sort(array,win):
    global array_accesses
    while(check_sorted(array) == False):
        pos1 = random.randrange(0,len(array))
        pos2 = random.randrange(0,len(array))
        array[pos1],array[pos2] = array[pos2],array[pos1]
        array_accesses += 4
        draw_screen(win,array, array_accesses)
        check_quit()

