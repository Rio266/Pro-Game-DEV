import pygame, random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alien Shooter Game")
space = pygame.image.load("images\\space.png")
space = pygame.transform.scale(space, (800, 600))
player_one = pygame.image.load("images\\triangle.png")
player = pygame.transform.scale(player_one, (100, 100))
player_x = 350
player_rect = player.get_rect(topleft = (player_x, 500))
target = pygame.image.load("images\\circle.png")
target = pygame.transform.scale(target, (50, 50))
keys = [False, False]
target_x = random.randint(0, 750)
target_y = 50
target_velocity = 0.4
target_rect = target.get_rect(topleft = (target_x, target_y))
bullet_velocity = 2
target_hit = pygame.USEREVENT + 1
run = True
bullets_list = []
score = 0
high_score = 0
game_over = False
font = pygame.font.SysFont("Georgia", 30, bold = True)
def draw(bullets):
    for i in bullets:
        pygame.draw.rect(screen, "red", i)
def bullet_handle(bullets):
    for i in bullets:
        i.y -= bullet_velocity
        if target_rect.colliderect(i):
            pygame.event.post(pygame.event.Event(target_hit))
            bullets_list.remove(i)
        elif i.y < 0:
            bullets_list.remove(i)
while run:
    player_rect.x  = player_x
    player_rect.y = 500
    screen.blit(space, (0, 0))
    screen.blit(player, player_rect)
    screen.blit(target, target_rect)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == target_hit:
            score += 1
            if score > high_score:
                high_score = score
            target_y = 50
            target_x = random.randint(0, 750)
            target_rect.x = target_x
            target_rect.y = target_y
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
               keys[0] = True
            elif i.key == pygame.K_RIGHT:
                keys[1] = True
            elif i.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_rect.centerx - 2, player_rect.top, 5, 10)
                bullets_list.append(bullet)
            if i.key == pygame.K_r and game_over:
                score = 0
                game_over = False
                target_y = 50
                target_x = random.randint(0, 750)
                target_rect.x = target_x
                target_rect.y = target_y
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT:
                keys[0] = False
            elif i.key == pygame.K_RIGHT:
                keys[1] = False
    if not game_over:
        if keys[0]:
            if player_x > 0:
                player_x -= 0.8
        elif keys[1]:
            if player_x < 700:
                player_x += 0.8
    if not game_over:
        target_y += target_velocity
        target_rect.y = target_y
        if target_y > 600:
            game_over = True
    draw(bullets_list)
    bullet_handle(bullets_list)
    if not game_over:
        score_text = font.render("Score: " + str(score), True, "white")
        # high_score_text = font.render("High Score: " + str(high_score), True, "white")
        screen.blit(score_text, (20, 20))
        # screen.blit(high_score_text, (20, 50))
    if game_over:
        game_over_text = font.render("GAME OVER", True, "red")
        final_score_text = font.render("Final Score: " + str(score), True, "white")
        high_score_text = font.render("High Score: " + str(high_score), True, "white")
        restart_text = font.render("Press R to restart", True, "white")
        screen.blit(game_over_text, (300, 250))
        screen.blit(final_score_text, (290, 300))
        screen.blit(high_score_text, (290, 350))
        screen.blit(restart_text, (270, 400))
    pygame.display.update()