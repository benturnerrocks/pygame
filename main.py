'''
main document for the recreation of the snake game
'''

import pygame
from pygame.locals import *
import sys
import random

# Creating a tuple to hold the RGB (Red, Green Blue) values
# So that we can paint our screen blue later
R,G,B = 255, 255, 255
screenColor = (R,G,B)

#we want to declare our grid to be 32 pixels wide since that is the size of our objects
grid_size = 32 
# Set game screen width and height to multiple of gridsize
grid_width, grid_height = 25, 20
screen_width, screen_height = grid_width * grid_size, grid_height * grid_size

up, down, left, right = (0,-1), (0,1), (-1,0), (1,0)

class Snake:
    def __init__(self):
        self.length = 1
        self.speed = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
        self.unif_color = (17,24,47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self,point):
        #if the snake is more than just point block, we cant turn backwards
        if self.length > 1 and (-1*point[0], -1*point[1]) == self.direction:
            return
        #otherwise, change the direction towards new point
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        #find where the head will move to
        new = (((cur[0]+(x*grid_size))%screen_width), (cur[1]+(y*grid_size))%screen_height)

        #actually move head and remove tail
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0
    
    def draw(self, surface):
        for part in self.positions:
            r = pygame.Rect((part[0], part[1]), (grid_size,grid_size))
            pygame.draw.rect(surface, self.unif_color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)
    
    def handle_keys(self):
        # Get feedback from the player in the form of events
        for event in pygame.event.get():
            # If the player clicks the red 'x', it is considered a quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
  
    def increaseSpeed(self, multiplier):
        self.speed *= multiplier

class Fish:
    def __init__(self):
        #self.sprite = pygame.image.load('data/gfx/fish.jpeg')
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*grid_size, random.randint(0, grid_height-1)*grid_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (grid_size, grid_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def draw_grid(surface):
    '''
    @func: draw the background grid
    @params: surface
    @output: nothing
    '''
    for y in range(0,int(grid_height)):
        for x in range(0,int(grid_width)):
            #make the grid checkered so we can see it
            if (x+y)%2==0:
                rec = pygame.Rect((x*grid_size,y*grid_size),(grid_size,grid_size))
                pygame.draw.rect(surface,(123,123,123),rec)

def main():
    # Initialize all of the Pygame modules so we can use them later on
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    snake = Snake()
    fish = Fish()

    myfont = pygame.font.SysFont("monospace",16)

    while True:
        clock.tick(10)
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        if snake.get_head_position() == fish.position:
            snake.length += 1
            snake.score += 1
            fish.randomize_position()
        snake.draw(surface)
        fish.draw(surface)
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()
        

if __name__ == "__main__":
    main()