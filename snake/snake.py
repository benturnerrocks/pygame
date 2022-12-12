import pygame
import sys
import random

class Snake():
    '''
        A class for the user-controlled snake within the game
    '''
    def __init__(self):
        '''
            @func: initializes all the important variables for our snake
            @params: None
            @output: None
        '''
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        # Special thanks to YouTubers Mini - Cafetos and Knivens Beast for raising this issue!
        # Code adjustment courtesy of YouTuber Elija de Hoog
        self.score = 0
        self.speed = 10
        self.keyboard = [up,down,left,right]

    def get_speed(self):
        '''
            @func: returns the current speed of the snake. The speed is implemented by changing the frame rate of the clock ticks in the game loop
            @params: None
            @output: speed (int)
        '''
        return self.speed

    def get_head_position(self):
        '''
            @func: returns the current position of the head of the snake
            @params: None
            @output: position (tuple of int)
        '''
        return self.positions[0]

    def get_tail_position(self):
        '''
            @func: returns the current position of the tail of the snake only if it has a tail
            @params: None
            @output: position (tuple of int)
        '''
        if self.length < 2:
            return (-1000,-1000)
        return self.positions[-1]

    def get_body_position(self):
        '''
            @func: returns the current position of each body part of the snake only if it has a body
            @params: None
            @output: array of positions (array of tuples of int)
        '''
        if self.length < 3:
            return []
        return self.positions[1:-1]

    def turn(self, point):
        '''
            @func: changes the direction towards given point heading but only if it is allowed given snake length
            @params: point (tuple of int between 1 and -1)
            @output: None
        '''
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        '''
            @func: updates the positions of the snake by adding a new head block on the front in the correct direction
            @params: None
            @output: None
        '''
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))), (cur[1]+(y*gridsize)))
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        elif new[0]>= screen_width or new[0] < 0 or new[1]>= screen_height or new[1] < 0:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        '''
            @func: resets the variables of the snake to their original values unless the old score is less than 0
            @params: None
            @output: None
        '''
        old_score = self.score
        self.__init__()
        self.score = min([old_score,self.score])
        pygame.mixer.Sound.play(dead_sfx)

    def draw_body(self,surface):
        '''
            @func: draws the body elements of the snake
            @params: surface (what we are drawing onto that space)
            @output: None
        '''
        if self.length < 3:
            return
        for p in self.get_body_position():
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def draw_head(self,surface):
        '''
            @func: draws the head of the snake
            @params: surface (what we are drawing onto that space)
            @output: None
        '''
        p = self.get_head_position()
        r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93,216, 228), r, 1)

    def draw_tail(self,surface):
        '''
            @func: draws the tail of the snake
            @params: surface (what we are drawing onto that space)
            @output: None
        '''
        if self.length < 2:
            return
        p = self.get_tail_position()
        r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93,216, 228), r, 1)


    def handle_keys(self):
        '''
            @func: gets all the events and checks if they are valid keyboard inputs (up,down,left,right) and turns the snake accordingly
            @params: None
            @output: None
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(self.keyboard[0])
                elif event.key == pygame.K_DOWN:
                    self.turn(self.keyboard[1])
                elif event.key == pygame.K_LEFT:
                    self.turn(self.keyboard[2])
                elif event.key == pygame.K_RIGHT:
                    self.turn(self.keyboard[3])
        
    def evil_action(self):
        '''
            @func: executes a random evil action that is meant to hinder the player (or if lucky help)
            @params: None
            @output: None
        '''
        action = random.randint(0,6)

        if action == 0:
            self.speed += 5
        elif action == 1:
            self.length += 5
        elif action == 2:
            self.score -= 10
        elif action == 3:
            self.reset()
        elif action == 4:
            self.keyboard = [down,up,right,left]
        elif action == 5:
            self.score += 10
        elif action == 6:
            pass
        

class Fish():
    '''
        A class for the consumables
    '''
    def __init__(self):

        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        '''
            @func: sets the consumable to a random position on the grid
            @params: None
            @output: None
        '''
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        '''
            @func: draws the graphic for the consumable into existance at its position
            @params: surface (different for different types of consumables)
            @output: None
        '''
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def get_position(self):
        '''
            @func: gets the position of the consumable
            @params: None
            @output: position (tuple of int)
        '''
        return self.position



def drawBackground(surface):
    '''
        @func: draw the background grid
        @params: surface
        @output: None
    '''
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
            pygame.draw.rect(surface,(255,255,255), r)


screen_width = 648
screen_height = 648

gridsize = 36
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)


def main():
    '''
        @func: the main function that actually runs the game
        @params: None
        @output: None
    '''
    pygame.init()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawBackground(surface)

    snake = Snake()
    head = pygame.image.load('/data/gfx/snake_head.jpg')
    body = pygame.image.load('data/gfx/snake_body.jpg')
    tail = pygame.image.load('data/gfx/snake_tail.jpg')
    food = Fish()
    fish = pygame.image.load('data/gfx/fish.jpg')
    evil_food = Fish()
    evil_fish = pygame.image.load('data/gfx/fish_evil.jpg')

    bad_sfx = pygame.mixer.Sound("data/sfx/Bad.wav")
    food_sfx = pygame.mixer.Sound("data/sfx/Food.wav")
    global dead_sfx 
    dead_sfx = pygame.mixer.Sound("data/sfx/Dead.wav")

    myfont = pygame.font.SysFont("monospace",16)

    while (True):
        clock.tick(snake.get_speed())
        snake.handle_keys()
        drawBackground(surface)
        snake.move()
        if snake.get_head_position() == food.get_position():
            snake.length += 1
            snake.score += 1
            food.randomize_position()
            pygame.mixer.Sound.play(food_sfx)
        elif snake.get_head_position() == evil_food.get_position():
            snake.evil_action()
            evil_food.randomize_position()
            pygame.mixer.Sound.play(bad_sfx)
            
        snake.draw_head(head)
        snake.draw_body(body)
        snake.draw_tail(tail)
        food.draw(fish)
        food.draw(surface)
        screen.blit(surface, (0,0))
        screen.blit(head, snake.get_head_position())
        for block in snake.get_body_position():
            screen.blit(body, block)
        screen.blit(tail, snake.get_tail_position())
        screen.blit(fish, food.get_position())
        screen.blit(evil_fish, evil_food.get_position())
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

if __name__ == "__main__":
    main()