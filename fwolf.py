import pygame
import random, sys
pygame.init()
WIDTH = 1000
HEIGHT = 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Wolf Game")
clock = pygame.time.Clock()
BLACK = (10, 10, 15)
WHITE = (255, 255, 255)
RED = (220, 50, 50)
GREY = (80, 80, 90)
DARK_GREY = (30, 30, 40)
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 80)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((45, 45))
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.health = 100
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, HEIGHT)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((35, 35))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        side = random.randint(0, 3)
        if side == 0:
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = -40
        elif side == 1:
            self.rect.x = WIDTH + 40
            self.rect.y = random.randint(0, HEIGHT)
        elif side == 2:
            self.rect.x = random.randint(0, WIDTH)
            self.rect.y = HEIGHT + 40
        else:
            self.rect.x = -40
            self.rect.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(1.5, 2.5)
    def update(self):
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max((dx ** 2 + dy ** 2) ** 0.5, 1)
        self.rect.x += int(dx / distance * self.speed)
        self.rect.y += int(dy / distance * self.speed)
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
score = 0
spawn_timer = 0
game_over = False
def Reset():
    global score, spawn_timer, game_over
    player.health = 100
    player.rect.center = (WIDTH // 2, HEIGHT // 2)
    for i in enemies:
        i.kill()
    enemies.empty()
    score = 0
    spawn_timer = 0
    game_over = False
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
              Reset()
    if not game_over:
        player.update()
        spawn_timer += 1
        if spawn_timer >= 60:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)
            spawn_timer = 0
        enemies.update()
        hits = pygame.sprite.spritecollide(
            player,
            enemies,
            True
        )
        if hits:
            player.health -= 10
            if player.health <= 0:
                game_over = True
        score += 1
    screen.fill(BLACK)
    all_sprites.draw(screen)
    health_text = font.render(
        f"Health: {player.health}",
        True,
        WHITE
    )
    screen.blit(health_text, (20, 20))
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )
    screen.blit(score_text, (20, 55))
    if game_over:
        game_over_text = big_font.render(
            "YOU DIED",
            True,
            RED
        )
        restart_text = font.render(
            "Press R to restart",
            True,
            WHITE
        )
        score_text = font.render(
            f"Final Score: {score}",
            True,
            WHITE
        )
        screen.blit(
            game_over_text,
            game_over_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 - 60)
            )
        )
        screen.blit(
            score_text,
            score_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 20)
            )
        )
        screen.blit(
            restart_text,
            restart_text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2 + 70)
            )
        )
    pygame.display.flip()
pygame.quit()
sys.exit()