#This is the file for the sorting algorithms and the smaller helper functions. 
from visuals import draw_screen, check_quit
from quick_sort import *
from bogo_sort import *
DELAY = 0

def find_smallest(array):
    smallest = array[0]
    for i in range (1,len(array)):
        if array[i] < smallest:
            smallest = array[i]
    return smallest

def selection_sort(array, win):
    for i in range(len(array)):
        smallest = i
        for k in range(i+1,len(array)):
            if array[k].height < array[smallest].height:
                smallest = k
        tmp = array[i]
        array[i] = array[smallest]
        array[smallest] = tmp
        draw_screen(win,array)
        check_quit()
        #pygame.time.wait(DELAY)
    return array

def bubble_sort(arr, win):  # Completes the bubble sort algorithm to order the list.
    for i in range(len(arr)-1):
        for k in range(len(arr) - 1 - i):
            check_quit()
            if arr[k].height > arr[k + 1].height:
                arr[k], arr[k + 1] = arr[k+1], arr[k]
                draw_screen(win, arr)
                #pygame.time.delay(DELAY)
    return arr

def insertion_sort(arr, win):
    for i in range(len(arr)):
        j = i
        while (j > 0 and arr[j].height < arr[j-1].height):
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
            draw_screen(win, arr)
            #pygame.time.delay(DELAY) 

