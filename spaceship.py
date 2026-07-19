import pygame
from pygame.locals import *
from time import *
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Spaceship")
run = True
space = pygame.image.load("images\\space_bg.jpg")
space = pygame.transform.scale(space, (400, 400))
rocket = pygame.image.load("images\\rocket.png")
rocket = pygame.transform.scale(rocket, (120, 120))
keys = [False, False, False, False]
rocket_x = 140
rocket_y = 140
while rocket_y < 400:
    screen.blit(space, (0, 0))
    screen.blit(rocket, (rocket_x, rocket_y))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys[0] = True
            elif i.key == K_DOWN:
                keys[1] = True
            elif i.key == K_LEFT:
                keys[2] = True
            elif i.key == K_RIGHT:
                keys[3] = True
        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys[0] = False
            if i.key == K_DOWN:
                keys[1] = False
            elif i.key == K_LEFT:
                keys[2] = False
            elif i.key == K_RIGHT:
                keys[3] = False
    if keys[0]:
        if rocket_y > 0:
            rocket_y -= 3
    if keys[1]:
        if rocket_y < 280:
            rocket_y += 3
    if keys[2]:
        if rocket_x > 0:
            rocket_x -= 3
    if keys[3]:
        if rocket_x < 280:
            rocket_x += 3
    rocket_y += 2
    sleep(0.05)