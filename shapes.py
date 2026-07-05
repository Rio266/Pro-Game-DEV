import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello")
run = True
class Rectangle():
    def __init__(self, color, x, y, w, h):
        self.c = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.screen = screen
    def draw_rectangle(self):
        pygame.draw.rect(self.screen, self.c, (self.x, self.y, self.w, self.h))
    def rectangle_grow(self, wid, hei):
        self.w += wid
        self.h += hei
        pygame.draw.rect(self.screen,self.c, (self.x, self.y, self.w, self.h))
rectangle_a = Rectangle("orange", 200, 200, 50, 30)
screen.fill("blue")
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONUP:
            rectangle_a.draw_rectangle()
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONDOWN:
            rectangle_a.rectangle_grow(5, 3)
            pygame.display.update()
        elif i.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            rectangle_b = Rectangle("red", pos[0], pos[1], 20, 20)
            rectangle_b.draw_rectangle()
            pygame.display.update()