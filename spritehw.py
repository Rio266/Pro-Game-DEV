import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Sprite")
run = True
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images\\banana.png")
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
class Sprite_orange(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_two = pygame.image.load("images\\orange.jpg").convert_alpha()
        self.image = pygame.transform.scale(self.image_two, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 0

    def update(self, keys_pressed):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 600:
            self.rect.right = 600
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
        
        if keys_pressed[pygame.K_UP]:
                self.rect.y -= 20
        if keys_pressed[pygame.K_DOWN]:
                self.rect.y += 20
        if keys_pressed[pygame.K_LEFT]:
                self.rect.x -= 20   
        if keys_pressed[pygame.K_RIGHT]:
                self.rect.x += 20 
group = pygame.sprite.Group()   
obj = Sprite()
obj_orange = Sprite_orange()
group.add(obj)
group.add(obj_orange)
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    screen.blit(pygame.image.load("images\\naturebg.png"), (0, 0))
    group.draw(screen)
    keys_pressed = pygame.key.get_pressed()
    obj.update(keys_pressed)
    obj_orange.update(keys_pressed)
    pygame.display.update()