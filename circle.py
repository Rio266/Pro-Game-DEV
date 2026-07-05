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
    def circle_grow(self, size):
        self.r += size
        pygame.draw.circle(self.screen, self.c, self.p, self.r)
circle_one = Circle("green", (100, 100), 50)
run = True
screen.fill("blue")
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONUP:
            circle_one.circle_grow(5)
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            circle_one.draw_circle()
            pygame.display.update()
        elif i.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            circle_two = Circle("red", (pos), 20)
            circle_two.draw_circle()
            pygame.display.update()