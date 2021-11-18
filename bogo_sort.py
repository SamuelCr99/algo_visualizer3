import random
from sorting_algo import draw_screen, check_quit

def check_sorted(array):
    for i in range(len(array)-1):
        if array[i].height > array[i+1].height:
            return False
    return True


def bogo_sort(array,win):
    while(check_sorted(array) == False):
        pos1 = random.randrange(0,len(array))
        pos2 = random.randrange(0,len(array))
        array[pos1],array[pos2] = array[pos2],array[pos1]
        draw_screen(win,array)
        check_quit()

