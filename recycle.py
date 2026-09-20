import pygame, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hello")
run = True
class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images\\bin.png")
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
class Non_recycle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images\\plasticbag.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
class Recycle(pygame.sprite.Sprite):
    def __init__(self, img):
        super.__init__()
        self.image = pygame.image.load("images\\" + img)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
images = ["box.png", "pencil.png", "bag.png"]
recycle_group = pygame.sprite.Group()
non_recycle_group = pygame.sprite.Group()
all_sprites_group = pygame.sprite.Group()
for i in range(50):
    obj = Recycle(random.choice(images))
    obj.rect.x = random.randint(0, 570)
    obj.rect.y = random.randint(0, 570)
    recycle_group.add(obj)
    all_sprites_group.add(obj)
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.display.update()