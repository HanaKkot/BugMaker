import pygame
import tkinter
import tkinter.messagebox
import numpy as np

from pygame.locals import *
import os, sys



SCREEN_WIDTH = 640
SCREEN_HEIGHT = 700  # Number of window pixel in horizontal and vertical direction

# Doodle class
class Doodle(object):

    def __init__(self):  #  Initialize parameters of doodle
        self.dy = 0  # Vertical Speed
        self.image = pygame.image.load(os.path.join(os.getcwd(),'image/hana.png'))  # Image
        self.rect = pygame.Rect(150, 300, 102, 106)  #  Rectangular
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0)  # Main Screen
        self.background = pygame.image.load(os.path.join(os.getcwd(),'image/background.png'))  # Background
        self.left_status = False
        self.right_status = False  # Two boolean parameter to control keyboard input
        self.h = 400

    def move(self):  #Move the doodle by the keyboard input
        if self.left_status:
            self.rect.x -= 6
        elif self.right_status:
            self.rect.x += 6
        else:
            pass
        
        return self.rect.x

    def edge_judgement(self, plat):  
        self.dy += 0.3
        self.rect.y += self.dy
        if  self.rect.bottom >= plat.rect.top and self.rect.left <= plat.rect.right-15 and self.rect.right >= plat.rect.left+15 and self.dy >= 0 :
            self.jump()
        
        if self.rect.x >= 650:  # Close to the edge
            self.rect.x = -100
        
        elif self.rect.x <= -100:
            self.rect.x = 640

        #if self.rect.y <= self.h and self.dy <= 0:
            #self.rect.y = self.h
            #plat.rect.y = plat.rect.y - self.dy

    def jump(self):
        self.dy = -11

    def display(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.image, self.rect)

    def gameover(self):
        if self.rect.top >= SCREEN_HEIGHT:
            print("laji")
        else:
            pass
    
    
        


def keyboard_control(mine):  # Keyboard input

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                mine.left_status = True
            if event.key == pygame.K_RIGHT :
                mine.right_status = True
            if event.key == pygame.K_p:
                print("Pause")

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mine.left_status = False
            if event.key == pygame.K_RIGHT:
                mine.right_status = False

# Plant class
class Plat(object):
    def __init__(self):
        self.dy = 0
        self.image = pygame.image.load(os.path.join(os.getcwd(),'image/plat.png'))
        self.rect = pygame.Rect(np.random.randint(200), np.random.randint(200), 60, 26)
        self.x = 0
        self.y = 0 # 用于存储位置

    def display(self, hana):
        hana.screen.blit(self.image, self.rect)


# main function
def main():
    pygame.init()
    doodle = Doodle()
    
    for i in range(20):
        plat = Plat()
        plat_list = []
        plat_list.append(plat)
    #pygame.mixer.music.load(os.path.join(os.getcwd(), ''))
    while True:
        pygame.time.Clock().tick(75)
        keyboard_control(doodle)
        doodle.move()
        doodle.edge_judgement(plat)             
        doodle.display()
        for i in range(len(plat_list)):
            plat_list[i].display(doodle)
        pygame.display.update()
        doodle.gameover()

        


while True: 
    main()