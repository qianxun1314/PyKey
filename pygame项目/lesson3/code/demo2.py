# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 11:31
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo2.py

import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((350, 500))
pygame.display.set_caption("Author：千与千寻")

ball1 = pygame.image.load("ball.png")
ball1_rect = Rect(0, 0, 111, 111)

ball2 = pygame.image.load("ball.png")
ball2_rect = Rect(200, 200, 111, 111)

score = 0
font = pygame.font.SysFont("arial", 40)
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == KEYDOWN:
            if event.key == K_a:
                ball1_rect = ball1_rect.move([-10, 0])
            elif event.key == K_d:
                ball1_rect = ball1_rect.move([10, 0])
            elif event.key == K_w:
                ball1_rect = ball1_rect.move([0, -10])
            elif event.key == K_s:
                ball1_rect = ball1_rect.move([0, 10])

    screen.fill((200, 100, 100))
    textScore = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(textScore, (200, 0))

    screen.blit(ball1, ball1_rect)

    if not ball1_rect.colliderect(ball2_rect):
        screen.blit(ball2, ball2_rect)
    else:
        score += 10


    pygame.display.update()