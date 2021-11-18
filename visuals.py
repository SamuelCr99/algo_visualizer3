import pygame
import random
from sorting_algo import *

pygame.font.init()

WIDTH, HEIGHT = 1400,800 #Height and width of the pygame window. 
BLOCK_WIDTH = 10
WIN = pygame.display.set_mode ((WIDTH,HEIGHT))


FONT_SIZE = 30
PHASE_FONT = pygame.font.SysFont('comicsans', FONT_SIZE)

class Block:
    def __init__(self, height, color):
        self.height = height
        self.color = color

#Draws the blocks and background onto the screen. 
def draw_screen(win, block_list):
    win.fill((255,255,255))

    for x in range(len(block_list)):
        block = pygame.Rect(x * BLOCK_WIDTH, HEIGHT - block_list[x].height, BLOCK_WIDTH, block_list[x].height)
        color = block_list[x].color
        pygame.draw.rect(WIN, color, block)
    font = PHASE_FONT.render("Number of array accessed: ", 1, (0,0,0))
    WIN.blit(font, (0, 10))
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
        height = random.randint(0, HEIGHT)
        red    = random.randint(0, 255)
        green  = random.randint(0, 255)
        blue   = random.randint(0, 255)
        color  = (red, green, blue)
        block_list.append(Block(height, (color)))
    return block_list

def menu(win):
    while(1):
        win.fill((255,255,255))
        
        
        
        pygame.display.update()
        check_quit()


def main():
    #menu(WIN)  
    block_list = create_blocks()
    #selection_sort(block_list,WIN)
    #bubble_sort(block_list,WIN)
    #insertion_sort(block_list,WIN)
    #quick_sort(block_list,WIN)
    #bogo_sort(block_list,WIN)
    while(1):
        draw_screen(WIN,block_list)
        check_quit()
        


if __name__ == '__main__':
    main()