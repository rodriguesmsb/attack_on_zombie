# -*- coding: utf-8 -*-

"""
Created on Thu Jun 11 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

import pygame
class World():
    def __init__(self, data, tile_size):

        tile_size = tile_size
        self.enemey_group = pygame.sprite.Group()

        self.background = pygame.image.load("img/graveyard/bg.png")
    
    
    def draw(self, screen):
        pygame.draw.line(screen, (255,0,0), (0,300),(1000,300))


    def draw_background(self, screen):
        screen.blit(source = self.background, dest = (0,0))
        
      
