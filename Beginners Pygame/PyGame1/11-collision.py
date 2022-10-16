'''collision detection'''
from turtle import distance
import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Background 
background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(800,600))

pygame.display.set_caption('COSMIC INVADERS')
icon = pygame.image.load('SteelHead.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('cosmic-invaders.png')
playerImg = pygame.transform.scale(playerImg,(80,80))
playerX = 365
playerY = 500
playerX_change = 0
playerY_change = 0

# Enemy 
enemyImg = pygame.image.load('BAD_GUY.png')
enemyImg = pygame.transform.scale(enemyImg,(60,60))
enemyX = random.randint(0,740)
enemyY = random.randint(0,300)
enemyX_change = 0.3
enemyY_change = 40

# Bullet 
# ready - you cannot see the bullet on the screen 
# fire - the bullet is currently moving 
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg,(32,32))
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 1
bullet_state = 'ready'

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 24, y + 10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    d = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if d < 27:
        return True
    else:
        return False

# Game Loop 
running = True
while running:

    screen.fill((0,0,30)) 
     
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            # if event.key == pygame.K_UP:
                # playerY_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            # if event.key == pygame.K_DOWN:
                # playerY_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    # get the current x coordinate of the spaceship 
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                # playerY_change = 0

    playerX += playerX_change

    if playerX <= -10:
        playerX = -10
    if playerX >= 730:
        playerX = 730

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    if playerY >= 522:
        playerY = 522
     
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change 
    if enemyX >= 730:
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = 'ready'

    if bullet_state is 'fire':
         fire_bullet(bulletX, bulletY)
         bulletY -= bulletY_change

    # Collision 
    collision = iscollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 500
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = random.randint(0,740)
        enemyY = random.randint(0,300)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
