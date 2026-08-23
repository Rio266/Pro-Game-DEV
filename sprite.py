import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sprite")
run = True
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images\\rocket.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
    def update(self, keys_pressed):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 600:
            self.rect.right = 600
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
        if keys_pressed[pygame.K_w]:
            self.rect.y -= 20
        if keys_pressed[pygame.K_s]:
            self.rect.y += 20
        if keys_pressed[pygame.K_a]:
            self.rect.x -= 20
        if keys_pressed[pygame.K_d]:
            self.rect.x += 20
group = pygame.sprite.Group()
obj = Sprite()
group.add(obj)
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.blit(pygame.image.load("images\\space.png"), (0, 0))
    group.draw(screen)
    keys_pressed = pygame.key.get_pressed()
    obj.update(keys_pressed)
    pygame.display.update()