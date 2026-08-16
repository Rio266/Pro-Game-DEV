import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alien Shooter Game")
space = pygame.image.load("images\\space.png")
space = pygame.transform.scale(space, (800, 600))
player_one = pygame.image.load("images\\triangle.png")
player = pygame.transform.scale(player_one, (100, 100))
target = pygame.image.load("images\\circle.png")
target = pygame.transform.scale(target, (50, 50))
keys = [False, False]
player_x = 350
target_x = 375
target_y = 50
target_velocity = 2
bullet_velocity = 8
target_hit = pygame.USEREVENT + 1
run = True
bullets_list = []
def draw(bullets):
    for i in bullets:
        pygame.draw.rect(screen, "red", i)
def bullet_handle(bullets):
    for i in bullets:
        i.y -= bullet_velocity
        if target.colliderect(i):
            pygame.event.post(pygame.event.Event(target_hit))
            bullets_list.remove(i)
        elif i.y < 0:
            bullets_list.remove(i)
while run:
    screen.blit(space, (0, 0))
    screen.blit(player, (player_x, 500))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
               keys[0] = True
            elif i.key == pygame.K_RIGHT:
                keys[1] = True
            elif i.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.x + player.width, player.y + player.height // 2 - 2, 10, 5)
                bullets_list.append(bullet)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                keys[0] = False
            elif i.key == pygame.K_RIGHT:
                keys[1] = False
    if keys[0]:
        if player_x > 0:
            player_x -= 0.8
    elif keys[1]:
        if player_x < 700:
            player_x += 0.8
    draw(bullets_list)
    bullet_handle(bullets_list)
    pygame.display.update()