# -*- coding: utf-8 -*-
# @Time    : 2018/6/27 09:57
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo1.py

import pygame
pygame.init()
screen = pygame.display.set_mode((350, 500))
pygame.display.set_caption("Author：千与千寻")
font = pygame.font.SysFont("arial", 40)
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill((200, 100, 100))
    textScore = font.render("Score: ", True, (0, 0, 0))
    screen.blit(textScore, (200, 0))
    pygame.display.update()