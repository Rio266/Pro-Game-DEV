import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Bulb Simulator on Pygame")
run = True
while run:
    screen.fill("blue")
    on = pygame.image.load("images\\bulb+on.png")
    on = pygame.transform.scale(on, (300, 300))
    off = pygame.image.load("images\\bulb+off.png")
    off = pygame.transform.scale(off, (300, 300))
    font = pygame.font.SysFont("Times New Roman", 40)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.blit(on, (50, 50))
            text = font.render("Bulb Is On", True, "white")
            screen.blit(text, (108, 8))
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            screen.blit(off, (50, 50))
            text = font.render("Bulb is Off", True, "white")
            screen.blit(text, (108, 8))
            pygame.display.update()