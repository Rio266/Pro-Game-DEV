import pygame
pygame.init()
w = 864
h = 936
ground_scroll = 0
scroll_speed = 4
fps = 60
clock = pygame.time.Clock()
flying = False
game_over = False
background = pygame.image.load("images\\flappy_bird_bg.png")
ground = pygame.image.load("images\\ground.png")
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Flappy Bird")
run = True
class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # super.init()
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            img = pygame.image.load(f"images\\bird_{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.click = False
    def update(self):
        if flying == True:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)
        if game_over == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.click = False
            self.counter += 1
            flap_cooldown = 5
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index], self.velocity * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
bird_group = pygame.sprite.Group()
flappy = Bird(100, int(h/2))
bird_group.add(flappy)

while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    screen.blit(background, (0, 0))
    bird_group.draw(screen)
    bird_group.update()
    screen.blit(ground, (ground_scroll, 768))
    if flappy.rect.bottom > 768:
        game_over  = True
        flying = False
    ground_scroll -= scroll_speed 
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    pygame.display.update()