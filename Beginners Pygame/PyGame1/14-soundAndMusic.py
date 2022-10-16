'''Adding sounds and background music'''
from tkinter import font
from turtle import distance
import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Background 
background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(800,600))

# Background sound 
mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption('TIME SHIFT COSMIC INVADERS')
icon = pygame.image.load('SteelHead.png')
pygame.display.set_icon(icon)

# Player 
playerImg = pygame.image.load('redmon.png')
playerImg = pygame.transform.scale(playerImg,(80,80))
playerX = 365
playerY = 500
playerX_change = 0
playerY_change = 0

# Enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    ei1 = pygame.image.load('BAD_GUY.png')
    enemyImg.append(pygame.transform.scale(ei1,(60,60)))
    enemyX.append(random.randint(0,740))
    enemyY.append(random.randint(0,300))
    enemyX_change.append(0.6)
    enemyY_change.append(40)

# Enemy2
enemyImg2 = []
enemyX2 = []
enemyY2 = []
enemyX_change2 = []
enemyY_change2 = []
num_of_enemies2 = 6

for j in range(num_of_enemies2):
    ei2 = pygame.image.load('BAD_GUY2.png')
    enemyImg2.append(pygame.transform.scale(ei2,(60,60)))
    enemyX2.append(random.randint(0,740))
    enemyY2.append(random.randint(0,300))
    enemyX_change2.append(-0.3)
    enemyY_change2.append(40)

# Bullet 
# ready - you cannot see the bullet on the screen 
# fire - the bullet is currently moving 
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg,(32,32))
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'

# Score 
score_value = 0
the_font = pygame.font.Font('freesansbold.ttf', 32) #(style, size)
textX = 10
textY = 15

def show_score(x, y):
    score = the_font.render('Score : ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def enemy2(x, y, j):
    screen.blit(enemyImg2[j], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 24, y + 10))

def iscollision(enemyX, enemyY, bulletX, bulletY):
    d1 = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if d1 < 27:
        return True
    else:
        return False

def iscollision2(enemyX2, enemyY2, bulletX, bulletY):
    d2 = math.sqrt((math.pow(enemyX2 - bulletX, 2)) + (math.pow(enemyY2 - bulletY, 2)))
    if d2 < 27:
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
                playerX_change = -1.5
            # if event.key == pygame.K_UP:
                # playerY_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            # if event.key == pygame.K_DOWN:
                # playerY_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
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
     
    # Enemy Movement 
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.6
            enemyY[i] += enemyY_change[i] 
        if enemyX[i] >= 730:
           enemyX_change[i] = -0.6
           enemyY[i] += enemyY_change[i]

        # Collision 
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 500
            bullet_state = 'ready'
            score_value += 2
            print(score_value)
            enemyX[i] = random.randint(0,740)
            enemyY[i] = random.randint(0,300)
        
        enemy(enemyX[i], enemyY[i], i)
    
    # Enemy2 Movement
    for j in range(num_of_enemies2):
        enemyX2[j] += enemyX_change2[j]
        if enemyX2[j] <= 0:
            enemyX_change2[j] = 0.3
            enemyY2[j] += enemyY_change2[j] 
        if enemyX2[j] >= 730:
            enemyX_change2[j] = -0.3
            enemyY2[j] += enemyY_change2[j]

        # Collision
        collision2 = iscollision2(enemyX2[j], enemyY2[j], bulletX, bulletY)
        if collision2:
            explosion_Sound2 = mixer.Sound('explosion.wav')
            explosion_Sound2.play()
            bulletY = 500
            bullet_state = 'ready'
            score_value += 1
            print(score_value)
            enemyX2[j] = random.randint(0,740)
            enemyY2[j] = random.randint(0,300)

        enemy2(enemyX2[j], enemyY2[j], j)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = 'ready'

    if bullet_state is 'fire':
         fire_bullet(bulletX, bulletY)
         bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
