# -*- coding: utf-8 -*-
# @Time    : 2018/6/26 00:13
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo3.py

import pygame
pygame.init()

screen = pygame.display.set_mode((350, 500))
pygame.display.set_caption("Author：千与千寻")
ball = pygame.image.load("ball.png")
bg = pygame.image.load("bg.jpg")
ball_x = 0
ball_y = 0
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill((200, 100, 100))
    ball_x += 1
    ball_y += 1
    screen.blit(bg, (0, 0))
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.update()
