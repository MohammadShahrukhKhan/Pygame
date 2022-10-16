'''title, logo and background color'''
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600)) #height and width

# title and logo 
pygame.display.set_caption('COSMIC INVADERS') #for the title
icon = pygame.image.load('SteelHead.png')
pygame.display.set_icon(icon) #for the icon
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,250,0)) #to set bgcolor / (R, G, B)
    pygame.display.update() # to update changes