import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello")
class Circle():
    def __init__(self, color, position, radius):
        self.c = color
        self.p = position
        self.r = radius
        self.screen = screen
    def draw_circle(self):
        pygame.draw.circle(self.screen, self.c, self.p, self.r)
circle_one = Circle("green", (100, 100), 50)
run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.fill("blue")
    circle_one.draw_circle()
    pygame.display.update()