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
    def __init__(self,x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        
        #variables assigments
        self.scale = scale
        self.x = x
        self.y = y

        #create a blank list to store images
        self.images_right = []
        self.images_left = []

        #create inde to iterate over images
        self.index = 0
        self.counter = 0
    

        #load image
        #load the images
        for num in range(1,11):
            img_path = "img/knight/Walk (" + str(num) + ").png"
            
            img_right = pygame.image.load(img_path)

            player_right = pygame.transform.scale(img_right,(img_right.get_width() // self.scale , 
                                                             img_right.get_height() // self.scale))

            #flip image 
            player_left = pygame.transform.flip(player_right, True, False)

            self.images_right.append(player_right)
            self.images_left.append(player_left)

        #get images from list to display on screen
        self.hero = self.images_right[self.index]
        self.rect = self.hero.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.width = self.hero.get_width()
        self.height = self.hero.get_height()
        self.direction = "right"
        
        
    
    def update_player_position(self, screen, screen_width, screen_height):
        dx = 0
    
        walk_speed = 5

        #draw a rect around char
        pygame.draw.rect(screen, (255,255,0), self.rect, 2)

    
        #get key press
        key = pygame.key.get_pressed()

        #Add left move
        if key[pygame.K_LEFT]:
            dx -= 5
            self.direction = "left"

        if key[pygame.K_RIGHT]:
            #change character position
            dx += 5
            self.direction = "right"

        #add code to star animation only if key is pressed
        if key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
            self.counter += 1
        
        #Add animation during the move
        if self.counter > walk_speed:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == "right":
                self.hero = self.images_right[self.index]

            if self.direction == "left":
                self.hero = self.images_left[self.index]

        #update player coordinate
        self.rect.x += dx
        
        
        #draw player on screen
        screen.blit(source = self.hero, dest = self.rect)

        

class male_zombie(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        
        #variables assigments
        self.scale = scale
        self.x = x
        self.y = y
        self.speed = speed

        #create a blank list to store images
        self.images_right = []
        self.images_left = []

        #create index to iterate over images
        self.index = 0

        #creater a timer to using during animation
        self.update_time = pygame.time.get_ticks()

        for num in range(1,11):
            img_path = "img/zombie/male/Walk (" + str(num) + ").png"
            
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

            









            


