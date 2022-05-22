import pygame
import random 
import time


pygame.init()

win = pygame.display.set_mode((1080, 720))

clock = pygame.time.Clock()
fps = 60 # Fps (120, 60, 30)
f = pygame.font.SysFont('kokila', 50)
f1 = pygame.font.SysFont('kokila', 20)

class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 60
        self.h = 80
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.speed = 4
        self.ups = 10
        self.fall_speed = 10
        self.ground = 600
        self.jump_c = 1
        self.up_speed = 0
        self.score = 0
        self.score_m = 0
    def draw(self):
        pygame.draw.rect(win, (60, 60, 60), (self.x, self.y, self.w, self.h))
        text = f"SCORE: {self.score}"
        win_text = f.render(str(text), 1, (0, 0, 0))
        win.blit(win_text, (800, 100))
    def grav(self):
        self.score_m += 1
        if self.score_m >= 5:
            self.score += 1
            self.score_m = 0
        if self.y + self.h != self.ground and self.up_speed == 0:
            if self.y + self.fall_speed > self.ground:
                self.y += 1
            if self.y + self.fall_speed <= self.ground:
                self.y += self.fall_speed
            self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if self.up_speed != 0:
            self.up_speed -= 1
            self.y -= self.ups
        if self.jump_c < 1 and self.jump_c != 1 and self.ground == self.y + self.h:
            self.jump_c += 1
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump_c > 0:
            self.up_speed = 30
            self.jump_c -= 1

class Object():
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    def draw(self):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.w, self.h))
    def move(self):
        self.x -= self.speed
        if self.x < 50:
            data.remove(self)

class Masters():
    def __init__(self):
        self.dist = 0
        self.min_d = 400
        self.speed = 8
    def create(self):
        if len(data) > 1:
            if data[0].x < 0 and len(data) < 2:
                data.append(Object(1100, 520, 40, 80, self.speed))
        else:
            data.append(Object(1100, 520, 40, 80, self.speed))


data = []
master = Masters()
pl = Player(400, 500)
Run = True
while Run:
        clock.tick(fps)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
        pygame.draw.rect(win, (255, 255, 255), (0, 0, 1080, 720))
        pygame.draw.rect(win, (30, 30, 30), (0, 600, 1080, 120))
        for i in data:
            i.move()
            i.draw()
        print (pl.y)
        master.create()
        pl.grav()
        pl.move()
        pl.draw()
        pygame.display.update()
