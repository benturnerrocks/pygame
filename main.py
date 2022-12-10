'''
main document for the recreation of the snake game
'''

import pygame
from pygame.locals import *
import sys
import game_objects

# Creating a tuple to hold the RGB (Red, Green Blue) values
# So that we can paint our screen blue later
R,G,B = 255, 255, 255
screenColor = (R,G,B)

#we want to declare our grid to be 32 pixels wide since that is the size of our objects
grid_size = 32 
# Set game screen width and height to multiple of gridsize
screen_width, screen_height = 25 * grid_size, 20 * grid_size
grid_width, grid_height = screen_width/grid_size, screen_height/grid_size

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
    # Make a clock
    clock = pygame.time.Clock()
    # Create the game screen
    screen = pygame.display.set_mode((screen_width,screen_height))
    # Set a caption to our window
    pygame.display.set_caption("Snake")
    # Draw a blue background onto our screen/window
    screen.fill(screenColor)
    surface = pygame.Surface(screen.get_size()).convert()
    draw_grid(surface)
    # Draw the now blue window to the screen
    pygame.display.update()

    #create instances of our objects
    

    # Create a loop that will keep the game running
    # Until the user decides to quit
    while True:
        # Get feedback from the player in the form of events
        for event in pygame.event.get():
            # If the player clicks the red 'x', it is considered a quit event
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()