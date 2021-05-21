#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *


class hero(pygame.sprite.Sprite):
    def __init__(self,x,y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.scale = scale
        img = pygame.image.load("img/knight/Walk (1).png")
        self.image = pygame.transform.scale(img, (img.get_width() // self.scale , img.get_height() // self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x ,self.y)

class male_zombie(pygame.sprite.Sprite):
    def __init__(self,x,y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.scale = scale
        img = pygame.image.load("img/zombie/male/Walk (1).png")
        self.image = pygame.transform.scale(img, (img.get_width() // self.scale , img.get_height() // self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x ,self.y)




            


