import pygame
from pygame.locals import *
import random
import numpy as np
pygame.init()
cell_size = 20
cell_vertical = 36
cell_horizontal = 72
cells = [[72,36]]
screen_width = cell_size*cell_horizontal
screen_length = cell_size*cell_vertical

screen = pygame.display.set_mode((screen_width, screen_length))
pygame.display.set_caption("Snake Game")

#define colors
background = (0,0,0)
body_inner = (80,90,100)
body_outer = (100,100,100)
grass = (69,139,0)
dirt = (139,69,19)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
sky = (142,229,238)
food_col = (200,50,50)


#define game variables
run = True
wall_matrix = np.zeros((cell_vertical,cell_horizontal))
print(wall_matrix)
direction = 1
food = [0, 0]
head = 0


#create snake
snake_pos = [[0,0]]

#create food
def create_food():
    food[0] = cell_size * random.randint(0,(screen_width / cell_size)-1)
    food[1] = cell_size * random.randint(0,(screen_length / cell_size)-1)
def draw_food():
    pygame.draw.rect(screen,food_col,(food[0],food[1],cell_size,cell_size))


def draw_snake():
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen,green,(x[0],x[1],cell_size,cell_size))
           # pygame.draw.rect(screen, blue, (x[0] + 1, x[1] , cell_size - 2, cell_size - 2))


def draw_screen():
   screen.fill(sky)

def draw_sun():
    for i in range (3,8):
        for x in range(8,3,-1):
            wall_matrix[i][x] = 3

def draw_grid():
    for i in range(0,screen_length,cell_size):
        pygame.draw.line(screen, red, (0, i), (screen_width, i), 1)
    for i in range(0,screen_width,cell_size):
        pygame.draw.line(screen, red, (i, 0), (i, screen_length), 1)
def create_wall(wall_matrix):
    for i in range(cell_vertical-5,cell_vertical):
        for x in range(0,cell_horizontal):
            wall_matrix[i][x] = 2
    for i in range(cell_vertical-4,cell_vertical):
        for x in range(0,cell_horizontal):
            wall_matrix[i][x] = 1




def draw_wall(wall_matrix):
    create_wall(wall_matrix)
    draw_sun()
    for i in range(0,cell_vertical):
        for x in range(0,cell_horizontal):
            if(wall_matrix[i][x] == 1):
                pygame.draw.rect(screen,dirt,(x*cell_size,i*cell_size,cell_size,cell_size))
            if(wall_matrix[i][x] == 2):
                pygame.draw.rect(screen,grass,(x*cell_size,i*cell_size,cell_size,cell_size))
            if (wall_matrix[i][x] == 3):
                pygame.draw.rect(screen, (255,215,0), (x * cell_size, i * cell_size, cell_size, cell_size))






def snake_move():
    if event.key == pygame.K_RIGHT:
        snake_pos[0][0] += cell_size
        if (snake_pos[0][0] > screen_width - cell_size):
            snake_pos[0][0] = 0
        print(snake_pos)
    if event.key == pygame.K_LEFT:
        snake_pos[0][0] -= cell_size
        if (snake_pos[0][0] < 0):
            snake_pos[0][0] = screen_width - cell_size
        print(snake_pos)
    if event.key == pygame.K_DOWN:
        snake_pos[0][1] += cell_size
        if (snake_pos[0][1] > screen_length - cell_size):
            snake_pos[0][1] = 0
        print(snake_pos)
    if event.key == pygame.K_UP:
        snake_pos[0][1] -= cell_size
        if (snake_pos[0][1] < 0):
            snake_pos[0][1] = screen_length - cell_size
        print(snake_pos)




print(snake_pos)
#setup loop with event handlers
while run:
    draw_screen()
    draw_wall(wall_matrix)
    #draw_grid()
    draw_snake()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            snake_move()


    pygame.display.update()
pygame.quit()

