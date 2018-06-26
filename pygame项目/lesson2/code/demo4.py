# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 10:10
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo4.py

import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((350, 500))
pygame.display.set_caption("Author：千与千寻")
ball = pygame.image.load("ball.png")
ball_rect = Rect(0, 0, 111, 111)
bg = pygame.image.load("bg.jpg")
is_running = True



while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == MOUSEBUTTONDOWN:
            button_pos = event.pos
            if ball_rect.collidepoint(button_pos):
                print("球被点击了")


    screen.fill((200, 100, 100))
    ball_rect = ball_rect.move([1, 1])
    screen.blit(bg, (0, 0))
    screen.blit(ball, ball_rect)
    pygame.display.update()

