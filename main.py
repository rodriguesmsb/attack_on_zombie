#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *
from characters import hero, male_zombie

#initialize pygame
pygame.init()

#set window dimension
screen_width = 1000
screen_height = int(0.8 * screen_width)
tile_size = 50
scale = 8

#define fps
fps = 60

#create window
screen = pygame.display.set_mode(size = (screen_width, screen_height))


#give a title to window
pygame.display.set_caption("Attack on Zombies")


#load background
background = pygame.image.load("img/graveyard/bg.png")

#create characters
knight = hero(x = 200, y = 200, scale = 8)
male_zombie = male_zombie(x = 150, y = 50, scale = 6)


def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


run = True



while run:
    screen.blit(source = background, dest = (0,0))
    screen.blit(source = knight.image, dest = knight.rect)
    screen.blit(source = male_zombie.image, dest = male_zombie.rect)
    draw_grid()

    #add a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #update the screen
    pygame.display.update()


pygame.quit()

