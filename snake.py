class SnakePart:
    def __init__(self, index):
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

    def addPart(self):
        self.snakeParts.append(SnakePart(self.length))
        self.length = len(self.snakeParts)

    def getCoords(self):
        return (self.x,self.y)
    
    def increaseSpeed(self, multiplier):
        self.speed *= multiplier
    
    def getLength(self):
        return self.length
    
    
class SnakeGame:
    def __init__(self) -> None:
        self.snake = Snake(2)
        

        