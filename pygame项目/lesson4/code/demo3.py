# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 16:19
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo3.py


import pygame
from pygame.locals import *
pygame.init()



class Background:

    def __init__(self, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.rect = Rect(self.x, self.y, 480, 852)
        self.image = pygame.image.load('bg.png')

    def display(self):      #渲染到屏幕上
        self.screen.blit(self.image, self.rect)

    def moveDownLoop(self):
        if self.rect.y > 852:
            self.rect.y = -852
        self.rect.y += 5

screen = pygame.display.set_mode((480, 852))
pygame.display.set_caption("Author：千与千寻")

bg1 = Background(0, 0)


is_running = True


while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    bg1.moveDownLoop()
    bg1.display()


    pygame.display.update()