import pygame
import random
from sorting_algo import *

pygame.font.init()

WIDTH, HEIGHT = 1000,1000 #Height and width of the pygame window. 
BLOCK_WIDTH = 1
WIN = pygame.display.set_mode ((WIDTH,HEIGHT))


FONT_SIZE = 25
PHASE_FONT = pygame.font.SysFont('ariel', FONT_SIZE)

name_list = ["Selection sort", "Bubble sort", "Insertion sort", "Quick sort", "Bogo sort"]

class Block:
    def __init__(self, height, color):
        self.height = height
        self.color = color
    def __gt__(self, other):
        return self.height > other.height
    def __lt__(self, other):
        return self.height < other.height
    def __eq__(self, other):
        return self.height == other.height

#Draws the blocks and background onto the screen. 
def draw_screen(win, block_list,array_accesses):
    win.fill((255,255,255))

    for x in range(len(block_list)):
        block = pygame.Rect(x * BLOCK_WIDTH, HEIGHT - block_list[x].height, BLOCK_WIDTH, block_list[x].height)
        color = block_list[x].color
        pygame.draw.rect(WIN, color, block)
    font = PHASE_FONT.render("Number of array accessed: " + str(array_accesses), 1, (0,0,0))
    WIN.blit(font, (0, 5))
    pygame.display.update()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

#Creates our blocks in an unsorted array of blocks, which will then be sorted.  
def create_blocks():
    amount_of_blocks = int(WIDTH / BLOCK_WIDTH)
    block_list = []
    for x in range(amount_of_blocks):
        height = random.randrange(0,HEIGHT)
        red    = 255*(height/HEIGHT)#random.randint(0, 255)
        green  = 60
        blue   = 255*(1-height/HEIGHT) #random.randint(0, 255)
        color  = (red, green, blue)
        block_list.append(Block(height, (color)))
    return block_list

def menu(block_list,win):
    win.fill((255,255,255))
    font = PHASE_FONT.render("Press:", 1, (0,0,0))
    win.blit(font, (5, 0))
    for i in range(len(name_list)):
        font = PHASE_FONT.render(str(i+1) + ". " + name_list[i], 1, (0,0,0))
        win.blit(font, (5, (i+1)*20))

    while(1):
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selection_sort(block_list,win)
                elif event.key == pygame.K_2:
                    bubble_sort(block_list,win)  
                elif event.key == pygame.K_3:
                    insertion_sort(block_list,win)  
                elif event.key == pygame.K_4:
                    quick_sort(block_list,win)  
                elif event.key == pygame.K_5:
                    bogo_sort(block_list,win)
                return
                               


def main(win):
    block_list = create_blocks()
    menu(block_list,win)  
    font = PHASE_FONT.render("Press R to restart", 1, (0,0,0))
    win.blit(font, (0, 20))
    pygame.display.update()


    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main(win) 
        


if __name__ == '__main__':
    main(WIN) 












 