import pygame
import sys
import random

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)
        # Special thanks to YouTubers Mini - Cafetos and Knivens Beast for raising this issue!
        # Code adjustment courtesy of YouTuber Elija de Hoog
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def get_tail_position(self):
        if self.length < 2:
            return (-1000,-1000)
        return self.positions[-1]

    def get_body_position(self):
        if self.length < 3:
            return []
        return self.positions[1:-1]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
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
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw_body(self,surface):
        if self.length < 3:
            return
        for p in self.get_body_position():
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def draw_head(self,surface):
        p = self.get_head_position()
        r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93,216, 228), r, 1)

    def draw_tail(self,surface):
        if self.length < 2:
            return
        p = self.get_tail_position()
        r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93,216, 228), r, 1)


    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def drawBackground(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            
            r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
            pygame.draw.rect(surface,(228,228,228), r)

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
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawBackground(surface)

    snake = Snake()
    head = pygame.image.load('data/gfx/snake_head.jpg')
    body = pygame.image.load('data/gfx/snake_body.jpg')
    tail = pygame.image.load('data/gfx/snake_tail.jpg')
    food = Food()
    fish = pygame.image.load('data/gfx/fish.jpg')

    myfont = pygame.font.SysFont("monospace",16)

    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawBackground(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw_head(head)
        snake.draw_body(body)
        snake.draw_tail(tail)
        food.draw(surface)
        screen.blit(surface, (0,0))
        screen.blit(head, snake.get_head_position())
        for block in snake.get_body_position():
            screen.blit(body, block)
        screen.blit(tail, snake.get_tail_position())
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

main()