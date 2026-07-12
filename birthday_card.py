import pygame, time
pygame.init()
paper = pygame.display.set_mode((600, 600))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    paper.fill("red")
    cake = pygame.image.load("images\\birthday_cake.png")
    cake = pygame.transform.scale(cake, (500, 500))
    paper.blit(cake, (50, 0))
    font = pygame.font.SysFont("Arial", 40)
    text = font.render("Happy Birthday!", True, "green")
    paper.blit(text, (200, 500))
    pygame.display.update()

    time.sleep(3)
    envelope = pygame.image.load("images\\birthday_envelope.jpg")
    envelope = pygame.transform.scale(envelope, (500, 500))
    paper.blit(envelope, (50, 0))
    pygame.display.update()

    time.sleep(3)
    gift = pygame.image.load("images\\birthday_gift.png")
    gift = pygame.transform.scale(gift, (500, 500))
    paper.blit(gift, (50, 0))
    pygame.display.update()
  
    time.sleep(3)
    hat = pygame.image.load("images\\birthday_hat.jpg")
    hat = pygame.transform.scale(hat, (500, 500))
    paper.blit(hat, (50, 0))
    pygame.display.update()
  
    time.sleep(3)