import pygame, time
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello")
run = True
while run:
    # for i in pygame.event.get():
    #     if i.type == pygame.QUIT:
    #         run = False
    screen.fill("blue")
    on = pygame.image.load("images\\bulb_on.jpg")
    on = pygame.transform.scale(on, (300, 300))
    screen.blit(on, (50, 50))
    font = pygame.font.SysFont("Times New Roman", 40)
    text = font.render("Bulb is On", True, "white")
    screen.blit(text, (108, 8))
    pygame.display.update()

    time.sleep(3)
    screen.fill("blue")
    off = pygame.image.load("images\\bulb_off.png")
    off = pygame.transform.scale(off, (300, 300))
    screen.blit(off, (50, 50))
    text = font.render("Bulb is Off", True, "white")
    screen.blit(text, (108, 8))
    pygame.display.update()

    time.sleep(3)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False