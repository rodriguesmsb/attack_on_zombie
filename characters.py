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


class hero(pygame.sprite.Sprite):
    def __init__(self,x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        
        #variables assigments
        self.alive = True
        self.scale = scale
        self.x = x
        self.y = y

        #jump variables
        self.jump = False
        self.jump_vel = 0
        self.in_air = True
        self.gravity = 1

        #attack variable
        self.attack_on_ground = False
    

        #create a blank list to store images
        self.images_right = []
        self.images_left = []

        #create inde to iterate over images
        self.index = 0
        self.counter = 0

        #creater a timer to using during animation
        self.update_time = pygame.time.get_ticks()

        #create a action count
        self.action = 0
    
        

        #load all imges for the player
        animtions_types = ["Idle", "Walk", "Jump", "Attack"]
        #path for images
        path = "img/knight/"
        for animation in animtions_types:
            #create a temporary empty list
            temp_list_right = []
            temp_list_left = []

            #count number of files in the folder
            number_of_images = len(gb.glob(path + animation + " *"))
            

            for num in range(1,number_of_images + 1):
                img_path =  "img/knight/" + animation + " (" + str(num) + ").png"
                img_right = pygame.image.load(img_path)
                player_right = pygame.transform.scale(img_right,(img_right.get_width() // self.scale , 
                                                                 img_right.get_height() // self.scale))
                #flip image 
                player_left = pygame.transform.flip(player_right, True, False)
                #add images to temp list
                temp_list_right.append(player_right)
                temp_list_left.append(player_left)
            
            #add temp list to animation list
            self.images_right.append(temp_list_right)
            self.images_left.append(temp_list_left)

       
        #get images from list to display on screen
        self.hero = self.images_right[self.action][self.index]
        self.rect = self.hero.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.width = self.hero.get_width()
        self.height = self.hero.get_height()
        self.direction = "right"
    


    def update_action(self, new_action):

        #check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action

            #update the animation settings
            self.index = 0
            self.update_time = pygame.time.get_ticks()

    def update_animation(self):

        #update animation
        #define a timer
        ANIMATION_COOLDOWN = 300
        

        #update image depending on index
        if self.direction == "right":
            self.hero = self.images_right[self.action][self.index]
        if self.direction == "left":
            self.hero = self.images_left[self.action][self.index]
                

        #check if enough time is passed since last update
        if (pygame.time.get_ticks() - self.update_time) > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.index += 1
           
                
        if self.index >= len(self.images_right[self.action]):
            self.index = 0
        
    

            
        
    
    def update_player_position(self, screen, screen_width, screen_height):
        dx = 0
        dy = 0
    
        walk_speed = 5
        print(self.action)

        #draw a rect around char
        pygame.draw.rect(screen, (255,255,0), self.rect, 2)


        if self.alive:

            #creating animation according to action (fix speeed animation next)
            if self.action == 0:
                self.update_animation()

            if self.action == 1:
                self.update_animation()

            if self.action == 2:
                self.update_animation()

            if self.action == 3:
                self.update_animation()

         

            

            #get key press
            key = pygame.key.get_pressed()



            #check for attack
            if key[pygame.K_SPACE] and self.jump == False and self.in_air == False:
                self.attack_on_ground = True
            if key[pygame.K_SPACE] == False:
                self.attack_on_ground = False
                
            #Add left move
            if key[pygame.K_LEFT]:
                dx -= 5
                self.direction = "left"

            if key[pygame.K_RIGHT]:
                #change character position
                dx += 5
                self.direction = "right"


            #add code to update action according to pressed key
            if key[pygame.K_RIGHT] or key[pygame.K_LEFT]:
                self.update_action(1)

            elif key[pygame.K_UP]:
                self.update_action(2)

            elif key[pygame.K_w]:
                self.update_action(3)

            else:
                self.update_action(0)


            if key[pygame.K_UP] and self.jump == False and self.in_air == False:
                self.jump_vel = -11
                self.jump = True
                self.in_air = True
                
               
                
            #stopping jum event
            if key[pygame.K_w] == False:
                self.jump = False
                
              

            self.jump_vel += self.gravity
            if self.jump_vel > 10:
                self.jump_vel = 0
            dy += self.jump_vel



            #check colision with flor
            if self.rect.bottom + dy > 300:
                dy = 300 - self.rect.bottom
                self.in_air = False
            
            
            

                    
    
          

        #end self alive
        else:
            pass
  


            
        #update player coordinate
        self.rect.x += dx
        self.rect.y += dy
        
        
        #draw player on screen
        screen.blit(source = self.hero, dest = self.rect)

        

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

    

            









            


