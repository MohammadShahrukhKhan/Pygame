'''Movement mechanics'''
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('COSMIC INVADERS')
icon = pygame.image.load('SteelHead.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('cosmic-invaders.png')
playerImg = pygame.transform.scale(playerImg,(55,55))
playerX = 370
playerY = 480

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True
while running:

    screen.fill((0,0,100)) 
    #value increases by the rate of number / if '-' sign entered then moves in opposite direction
    playerX += 0.1
    playerY -= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()
