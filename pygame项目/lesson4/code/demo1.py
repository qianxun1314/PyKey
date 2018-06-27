# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 14:11
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo1.py

import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((480, 852))
pygame.display.set_caption("Author：千与千寻")


bg1 = pygame.image.load("bg.png")
bg1_rect = Rect(0, 0, 480, 852)

bg2 = pygame.image.load("bg.png")
bg2_rect = Rect(0, -852, 480, 852)

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    bg1_rect = bg1_rect.move([0, 5])
    bg2_rect = bg2_rect.move([0, 5])

    if bg1_rect.y > 852:
        bg1_rect.y = -852
    if bg2_rect.y > 852:
        bg2_rect.y = -852

    screen.blit(bg1, bg1_rect)
    screen.blit(bg2, bg2_rect)


    pygame.display.update()