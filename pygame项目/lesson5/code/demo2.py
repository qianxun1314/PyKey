# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 08:37
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo2.py

import pygame
from pygame.locals import *
pygame.init()


class Sprite:
    def __init__(self, x, y, img_path, w, h):
        self.screen = screen
        self.x = x
        self.y = y
        self.ima_path = img_path
        self.rect = Rect(self.x, self.y, w, h)
        self.image = pygame.image.load(img_path)

    def display(self):
        self.screen.blit(self.image, self.rect)

class Background(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self, x, y, "imgs/bg.png", 480, 852)


    def moveDownLoop(self):
        if self.rect.y > 852:
            self.rect.y = -852
        self.rect.y += 5


class Hero(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self, x, y, "imgs/hero.png", 100, 124)

    def moveLeft(self):
        self.rect.x -= 30
    def moveRight(self):
        self.rect.x += 30


screen = pygame.display.set_mode((480, 852))
pygame.display.set_caption("Author：千与千寻")

bg1 = Background(0, 0)
bg2 = Background(0, -852)

hero = Hero(200, 600)
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == KEYDOWN:
            if event.key == K_a:
                hero.moveLeft()
            elif event.key == K_d:
                hero.moveRight()


    bg1.moveDownLoop()
    bg1.display()
    bg2.moveDownLoop()
    bg2.display()

    hero.display()
    pygame.display.update()