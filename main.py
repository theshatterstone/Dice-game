import random
import time
#setting up pygame
import pygame 
from pygame.locals import *
pygame.font.init()
pygame.init()

#setting up display
screen_width = 800
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Caveman') #Game title and icon go here

game_icon = pygame.image.load('img/CavemanIcon.png')
pygame.display.set_icon(game_icon)


#Change FPS

FPS = 60

#loading images
bg_img = pygame.transform.scale(pygame.image.load('img/new-bg.jpg'), (screen_width, screen_height) )
