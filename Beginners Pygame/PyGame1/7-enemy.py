'''adding the Enemy'''
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('COSMIC INVADERS')
icon = pygame.image.load('SteelHead.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('cosmic-invaders.png')
playerImg = pygame.transform.scale(playerImg,(80,80))
playerX = 365
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy 
enemyImg = pygame.image.load('BAD_GUY.png')
enemyImg = pygame.transform.scale(enemyImg,(60,60))
enemyX = random.randint(0,740)
enemyY = random.randint(0,430)
enemyX_change = 0
enemyY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

running = True
while running:

    screen.fill((0,0,30)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    if playerX >= 745:
        playerX = 745

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    if playerY >= 545:
        playerY = 545

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
