# -*- coding: utf-8 -*-
# @Time    : 2018/6/25 21:12
# @Author  : 千と千寻
# @Email   : pp2677345028@gmail.com
# @File    : demo1.py



import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    screen.fill((200, 100, 100))
    pygame.display.update()