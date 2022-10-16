'''Adding Boundaries'''
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
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True
while running:

    screen.fill((0,0,50)) 

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
    pygame.display.update()
