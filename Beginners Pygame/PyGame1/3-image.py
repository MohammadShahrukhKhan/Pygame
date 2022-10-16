'''adding image'''
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('COSMIC INVADERS')
icon = pygame.image.load('SteelHead.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('cosmic-invaders.png')
playerImg = pygame.transform.scale(playerImg,(55,55)) #to change the size of the image
playerX = 370 #for x coordinate
playerY = 480 #for y coordinate

def player():
    screen.blit(playerImg, (playerX, playerY))

running = True
while running:

    screen.fill((0,0,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player() # player should be called after screen.fill(()) method
    pygame.display.update()
