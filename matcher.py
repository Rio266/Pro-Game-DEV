import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Matcher")
ludo = pygame.image.load("images\\ludo.png")
subwaysurfers = pygame.image.load("images\\subwaysurfers.png")
templerun = pygame.image.load("images\\templerun.png")
candycrush = pygame.image.load("images\\candycrush.jpg")
font = pygame.font.SysFont("Arial", 30)#
game_one = font.render("Ludo", True, "black")
game_two = font.render("Subway Surfers", True, "black")
game_three = font.render("Temple Run", True, "black")
game_four = font.render("Candy Crush", True, "black")
run = True
screen.fill("white")
screen.blit(ludo, (100, 100))
screen.blit(subwaysurfers, (100, 200))
screen.blit(templerun, (100, 300))
screen.blit(candycrush, (100, 400))
screen.blit(game_one, (300, 300))
screen.blit(game_two, (300, 400))
screen.blit(game_three, (300, 100))
screen.blit(game_four, (300, 200))
while run:
    i = pygame.event.poll()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    if i.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, "green", (pos), 20)
        pygame.display.update()
    elif i.type == pygame.MOUSEBUTTONUP:
        pos_one = pygame.mouse.get_pos()
        pygame.draw.line(screen, "green", (pos), (pos_one), 3)
        pygame.draw.circle(screen, "green", (pos_one), 20)
        pygame.display.update()
    pygame.display.update()