# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 23:50
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo2.py


import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Author：千与千寻")
ball = pygame.image.load("ball.png")
ball_x = 0
ball_y = 0
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill((200, 100, 100))
    ball_x += 1
    screen.blit(ball, (ball_x, ball_y))
    pygame.display.update()