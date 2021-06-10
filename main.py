#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *
from characters import hero, zombie

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
knight = hero(x = 100, y = screen_height - 130, scale = 8)
zombie = zombie(x = 0, y = screen_height - 130, scale = 6, speed = 1, gender = "M")


def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


run = True



while run:
    screen.blit(source = background, dest = (0,0))
    draw_grid()

    
    knight.update_player_position(screen = screen, 
                                  screen_width = screen_width, 
                                  screen_height = screen_height)

    zombie.update_animation(screen = screen, 
                            screen_width = screen_width, 
                            screen_height = screen_height)

    #add a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    
    #update the screen
    pygame.display.update()


pygame.quit()

