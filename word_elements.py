
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr 15 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

## Import necessary libraries
import pygame
from pygame.locals import *
import glob as gb

class zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, gender):
        pygame.sprite.Sprite.__init__(self)
        
        #variables assigments
        self.scale = scale
        self.x = x
        self.y = y
        self.speed = speed
        self.action = 0

        #create a blank list to store images
        self.images_right = []
        self.images_left = []

        #create index to iterate over images
        self.index = 0

        #creater a timer to using during animation
        self.update_time = pygame.time.get_ticks()

        if gender == "M":
            zombie_path = "img/zombie/male/Walk ("
        elif gender == "F":
            zombie_path = "img/zombie/female/Walk ("


        for num in range(1,11):
            img_path =  zombie_path + str(num) + ").png"
            
            img_right = pygame.image.load(img_path)

            char_right = pygame.transform.scale(img_right,(img_right.get_width() // self.scale , 
                                                             img_right.get_height() // self.scale))

            #flip image 
            char_left = pygame.transform.flip(char_right, True, False)

            self.images_right.append(char_right)
            self.images_left.append(char_left)

        #get images from list to display on screen
        self.zombie = self.images_right[self.index]
        self.rect = self.zombie.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.width = self.zombie.get_width()
        self.height = self.zombie.get_height()
        self.direction = "right"

    
    def update_animation(self, screen, screen_width, screen_height):

        #define a timer
        ANIMATION_COOLDOWN = 100

        #update image depending on index
        self.images  = self.images_right[self.index]

        dx = 0
    

        #check if enough time is passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.index += 1
            
            if self.index >= len(self.images_right):
                self.index = 0
            dx += self.speed
        
            
        #update player coordinate
        self.rect.x += dx

        
        screen.blit(source = self.images, dest = self.rect)
