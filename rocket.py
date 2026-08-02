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
            if i.key == K_LSHIFT:
                keys[0] = True
        if i.type == pygame.KEYUP:
            if i.key == K_LSHIFT:
                keys[0] = False
    if keys[0]:
        if rocket_y > 0:
            rocket_y -= 7
    rocket_y += 3
    sleep(0.05)