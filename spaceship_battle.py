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
    for i in red_bullets:
        pygame.draw.rect(screen, "red", i)
    for i in yellow_bullets:
        pygame.draw.rect(screen, "yellow", i)
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
def bullet_handle(yellow_bullets, red_bullets, yellow, red):
    for i in yellow_bullets:
        i.x += bullet_velocity
        if red.colliderect(i):
            pygame.event.post(pygame.event.Event(red_hit))
            yellow_bullets.remove(i)
        elif i.x > 600:
            yellow_bullets.remove(i)
    for i in red_bullets:
        i.x -= bullet_velocity
        if yellow.colliderect(i):
            pygame.event.post(pygame.event.Event(yellow_hit))
            red_bullets.remove(i)
        elif i.x < 0:
            red_bullets.remove(i)
def game_over(text):
    t = font.render(text, 1, "grey")
    screen.blit(t, (600/2 - t.get_width()/2, 600/2 - t.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
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
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_q and len(yellow_bullets) < max_bullets:
                bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                yellow_bullets.append(bullet)
                fire.play()
            if i.key == pygame.K_e and len(red_bullets) < max_bullets:
                bullet = pygame.Rect(red.x, red.y + red.height//2 -2, 10, 5)
                red_bullets.append(bullet)
                fire.play()
        if i.type == red_hit:
            red_health -= 1
            hit.play()
        if i.type == yellow_hit:
            yellow_health -= 1
            hit.play()
    winner = ""
    if red_health == 0:
        winner = "Yellow Has Won!"
    if yellow_health == 0:
        winner = "Red Has Won!"
    if winner != "":
        game_over(winner)
        break
    draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    keys_pressed = pygame.key.get_pressed()
    yellow_movement(keys_pressed, yellow)
    red_movement(keys_pressed, red)
    bullet_handle(yellow_bullets, red_bullets, yellow, red)
    pygame.display.update()