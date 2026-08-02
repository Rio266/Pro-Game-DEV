import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Spaceship Game")
border = pygame.Rect(600/2 - 5, 0, 10, 600)
fire = pygame.mixer.Sound("images\\Gun+Silencer.mp3")
hit = pygame.mixer.Sound("images\\Grenade+1.mp3")
red_spaceship = pygame.image.load("images\\fighter_red.png")
yellow_spaceship = pygame.image.load("images\\fighter_yellow.png")
spaceship_width = 55
spaceship_height = 40
fps = 60
velocity = 5
bullet_velocity = 7
max_bullets = 3
font = pygame.font.SysFont("Arial", 20)
yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (spaceship_width, spaceship_height)), 270)
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship, (spaceship_width, spaceship_height)), 90)
space = pygame.transform.scale(pygame.image.load("images\space.png"), (600, 600))
run = True
def draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    screen.blit(space, (0, 0))
    pygame.draw.rect(screen, "black", border)
    red_health_text = font.render("health " + str(red_health), 1, "white")
    yellow_health_text = font.render("health " + str(yellow_health), 1, "white")
    screen.blit(red_health_text, (600 - red_health_text.get_width() - 10, 10))
    screen.blit(yellow_health_text, (10, 10))
    screen.blit(yellow_spaceship, (yellow.x, yellow.y))
    screen.blit(red_spaceship, (red.x, red.y))
    pygame.display.update()
def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - velocity > 0:
        yellow.x -= velocity
    elif keys_pressed[pygame.K_d] and yellow.x + velocity + yellow.width < border.x:
        yellow.x += velocity
    elif keys_pressed[pygame.K_w] and yellow.y - velocity > 0:
        yellow.y -= velocity
    elif keys_pressed[pygame.K_s] and yellow.y + velocity + yellow.height < 600 - 15:
        yellow.y += velocity
def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - velocity > border.x + border.width:
        red.x -= velocity
    if keys_pressed[pygame.K_RIGHT] and red.x + velocity + red.width < 600:
        red.x += velocity
    if keys_pressed[pygame.K_UP] and red.y - velocity > 0:
        red.y -= velocity
    if keys_pressed[pygame.K_DOWN] and red.y + velocity + red.height < 600 - 15:
        red.y += velocity
red = pygame.Rect(400, 400, spaceship_width, spaceship_height)
yellow = pygame.Rect(100, 400, spaceship_width, spaceship_height)
red_bullets = []
yellow_bullets = []
red_health = 10
yellow_health = 10
clock = pygame.time.Clock()
while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    keys_pressed = pygame.key.get_pressed()
    yellow_movement(keys_pressed, yellow)
    red_movement(keys_pressed, red)
    pygame.display.update()