#This is the file for the sorting algorithms and the smaller helper functions. 
from visuals import draw_screen, check_quit
from quick_sort import *
from bogo_sort import *
DELAY = 0

array_accesses = 0

def find_smallest(array):
    smallest = array[0]
    for i in range (1,len(array)):
        if array[i] < smallest:
            smallest = array[i]
    return smallest

def selection_sort(array, win):
    global array_accesses
    for i in range(len(array)):
        smallest = i
        for k in range(i+1,len(array)):
            array_accesses += 2
            if array[k] < array[smallest]:
                smallest = k
        array[i],array[smallest] = array[smallest],array[i]
        draw_screen(win,array,array_accesses)
        check_quit()
        #pygame.time.wait(DELAY)


def bubble_sort(arr, win):  # Completes the bubble sort algorithm to order the list.
    global array_accesses
    for i in range(len(arr)-1):
        for k in range(len(arr) - 1 - i):
            check_quit()
            if arr[k] > arr[k + 1]:
                array_accesses += 4
                arr[k], arr[k + 1] = arr[k+1], arr[k]
                draw_screen(win, arr,array_accesses)
                #pygame.time.delay(DELAY)


def insertion_sort(arr, win):
    global array_accesses
    for i in range(len(arr)):
        j = i
        while (j > 0 and arr[j] < arr[j-1]):
            array_accesses +=4
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1
            check_quit()
        draw_screen(win, arr, array_accesses) 

