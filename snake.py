import pygame
import random
from enum import Enum

WIDTH = 800
HEIGHT = 800

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4

class Food:
    x = 0
    y = 0
    
    def __init__(self):
        self.respawn()
    
    def respawn(self):
        self.x = random.randrange(0, WIDTH, WIDTH / 10)
        self.y = random.randrange(0, HEIGHT, HEIGHT / 10)

class Snake:
    x = 0
    y = 0
    x = random.randrange(0, WIDTH, WIDTH / 10)
    y = random.randrange(0, HEIGHT, HEIGHT / 10)
    tail = [(x,y)]

    def __init__(self):
        self.xSpeed = WIDTH / 10
        self.ySpeed = 0

    def updatePosition(self, food):
        i = len(self.tail)
        while i > 1:
            self.tail[i-1] = self.tail[i-2]
            i-=1
        self.x += self.xSpeed
        self.y += self.ySpeed
        self.checkFood(food)
        if self.x > WIDTH - WIDTH / 10:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH - WIDTH / 10
        if self.y > HEIGHT - HEIGHT / 10:
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT - HEIGHT / 10
        self.tail[0] = (self.x, self.y)
        self.checkCollision()

    def checkFood(self, food):
       tailLen = len(self.tail)
       for part in self.tail:
           if part[0] == food.x and part[1] == food.y:
               self.tail.append((self.tail[tailLen-1][0], self.tail[tailLen-1][1]))
               food.respawn()

    def changeDirection(self, direction):
        if direction == Direction.RIGHT:
            if self.xSpeed == 0:
                self.xSpeed = WIDTH / 10
                self.ySpeed = 0
        if direction == Direction.LEFT:
            if self.xSpeed == 0:
                self.xSpeed = -WIDTH / 10
                self.ySpeed = 0
        if direction == Direction.UP:
            if self.ySpeed == 0:
                self.ySpeed = -HEIGHT / 10
                self.xSpeed = 0
        if direction == Direction.DOWN:
            if self.ySpeed == 0:
                self.ySpeed = HEIGHT / 10
                self.xSpeed = 0

    def checkCollision(self):
        for part in self.tail:
        for part in self.tail[1:]:
            if self.tail[0] == part:
                self.reset()

    def reset(self):
        self.tail = self.tail[:3]
 
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    done = False
    s = Snake()
    f = Food()

    while not done:
            pygame.time.Clock().tick(10)
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True

            pressedKey = pygame.key.get_pressed()
            if pressedKey[pygame.K_RIGHT]:
                s.changeDirection(Direction.RIGHT)
            if pressedKey[pygame.K_LEFT]:
                s.changeDirection(Direction.LEFT)
            if pressedKey[pygame.K_UP]:
                s.changeDirection(Direction.UP)
            if pressedKey[pygame.K_DOWN]:
                s.changeDirection(Direction.DOWN)

            screen.fill((0,0,0))
            pygame.draw.rect(screen, (255,255,255), (s.tail[0][0],s.tail[0][1], (WIDTH / 10) - 1, (HEIGHT / 10) - 1))
            for part in s.tail[1:]:
                pygame.draw.rect(screen, (255,0,0), (part[0],part[1], (WIDTH / 10) - 1, (HEIGHT / 10) - 1))
            pygame.draw.rect(screen, (0,255,0), (f.x, f.y, WIDTH / 10, HEIGHT / 10))
            s.updatePosition(f)
            pygame.display.flip()
