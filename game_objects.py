import pygame

class SnakePart:
    def __init__(self, index):
        position = pygame.Vector2()
        position.xy = 295, 100
        velocity = pygame.Vector2()
        velocity.xy = 3, 0
        acceleration = 0.1
        rightSprite = pygame.image.load('data/gfx/player.png')
        leftSprite = pygame.transform.flip(rightSprite, True, False)
        currentSprite = rightSprite
        self.index = index
        self.width = 10
        self.height = 10
        self.image = "snake.jpeg"


class Snake:
    def __init__(self, length):
        self.length = length
        self.speed = 1
        self.x = 1
        self.y = 1
        self.snakeParts = []
        for i in range(self.length):
            self.snakeParts.append(SnakePart(i))

    def get_head_position(self):
        pass

    def turn(self):
        pass

    def move(self):
        pass

    def reset(self):
        pass
    
    def draw(self):
        pass
    
    def handlekeys(self):
        pass
    

    
    def add_part(self):
        self.snakeParts.append(SnakePart(self.length))
        self.length = len(self.snakeParts)

    def getCoords(self):
        return (self.x,self.y)
    
    def increaseSpeed(self, multiplier):
        self.speed *= multiplier
    
    def getLength(self):
        return self.length
    

class Fish:
    def __init__(self):
        self.sprite = pygame.image.load('data/gfx/fish.jpeg')
        self.position = pygame.Vector2()
        self.position.xy
    
    def randomize_position(self):
        pass

    def draw(self):
        pass

class BadFish(Fish):
    def __init__(self):
        self.sprite = pygame.image.load('data/gfx/fish.jpeg')
        self.position = pygame.Vector2()
        self.position.xy
