import pygame
import random
from sorting_algo import *

WIDTH, HEIGHT = 800,800 #Height and width of the pygame window. 
BLOCK_WIDTH = 1
WIN = pygame.display.set_mode ((WIDTH,HEIGHT))

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
    pygame.display.update()

def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()   

#Creates our blocks in an unsorted way. 
def create_blocks():
    amount_of_blocks = int(WIDTH / BLOCK_WIDTH)
    block_list = []
    for x in range(amount_of_blocks):
        height = random.randint(0, HEIGHT)
        red    = random.randint(0, 255)
        green  = random.randint(0, 255)
        blue   = random.randint(0, 255)
        color  = (red, green, blue)
        block_list.append(Block(height, color))
    return block_list

def main():
    block_list = create_blocks()
    while(1):
        selection_sort(block_list,WIN)
        #bubble_sort(block_list,WIN)
        #insertion_sort(block_list,WIN)
        


if __name__ == '__main__':
    main()