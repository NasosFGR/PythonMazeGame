import pygame

pygame.init() #ξεκινάει το εργοστάσιο pygame
screen = pygame.display.set_mode((1099, 900))
done = False
x1=30
y1=30
x2=1000
y2=30

clock = pygame.time.Clock()
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    pressed = pygame.key.get_pressed()  # Φτιάχνει μεταβλητή pressed που παίρνει σαν τιμή το πλήκτρο που πατήσαμε
    if pressed[pygame.K_UP]: y1 -= 3  # Αν πατιέται το ΠΑΝΩ βέλος, άλλαξε το Υ κατά -3
    if pressed[pygame.K_DOWN]: y1 += 3  # Αν πατιέται το ΚΑΤΩ βέλος
    if pressed[pygame.K_LEFT]: x1 -= 3  # Αν πατιέται το ΑΡΙΣΤΕΡΟ βέλος
    if pressed[pygame.K_RIGHT]: x1 += 3  # Αν πατιέται το ΔΕΞΙ βέλος

    if pressed[pygame.K_w]: y2 -= 3
    if pressed[pygame.K_s]: y2 += 3
    if pressed[pygame.K_a]: x2 -= 3
    if pressed[pygame.K_d]: x2 += 3



    screen.fill((0, 0, 0, 0))
    player1=pygame.draw.rect(screen,(0, 128, 255), pygame.Rect(x1, y1, 60, 60))
    player2 = pygame.draw.rect(screen, (204, 204, 0), pygame.Rect(x2, y2, 60, 60))
    player3 = pygame.draw.rect(screen, (57, 168, 45 ), pygame.Rect(400, 55, 60, 60))
    w1 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(100, 0, 60, 600))
    w2 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(300, 100, 30, 600))
    w3 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(900, 50, 30, 100))
    w4 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(400, 100, 90, 300))
    w5 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(900, 200, 42, 400))
    w6 = pygame.draw.rect(screen, (184, 84, 57), pygame.Rect(600, 600, 300, 200))

    if player1.bottom+0.5 > screen.get_rect().bottom:
        y1 -= 3
    if player1.top-0.5 < screen.get_rect().top:
        y1 += 3
    if player1.left > screen.get_rect().left:
        x1 -= 3
    if player1.right < screen.get_rect().right:
        x1 += 3
    if player2.bottom+0.5 > screen.get_rect().bottom:
        y2 -= 3
    if player2.top-0.5 < screen.get_rect().top:
        y2 += 3
    if player2.left > screen.get_rect().left:
        x2 -= 3
    if player2.right < screen.get_rect().right:
        x2 += 3

    Font = pygame.font.SysFont("comicsansms", 170 , True, True)

    Title = Font.render("Maze Finder",True,(39, 40, 39))

    screen.blit(Title, (9, 8))


    Font = pygame.font.SysFont("comicsansms", 50, True, True)

    Credits = Font.render("Created by Nasos", True, (39, 40, 39))

    screen.blit(Credits, (0, 10))

    if player1.colliderect(w1) or player1.colliderect(w2) or player1.colliderect(w3) or player1.colliderect(w4) or player1.colliderect(w5) or player1.colliderect(w6):
        if pressed[pygame.K_UP]: y1 += 3
        if pressed[pygame.K_DOWN]: y1 -= 3
        if pressed[pygame.K_LEFT]: x1 += 3
        if pressed[pygame.K_RIGHT]: x1 -= 3

    if player2.colliderect(w1) or player2.colliderect(w2) or player2.colliderect(w3) or player2.colliderect(w4) or player2.colliderect(w5) or player2.colliderect(w6):
        if pressed[pygame.K_w]: y2 += 3
        if pressed[pygame.K_s]: y2 -= 3
        if pressed[pygame.K_a]: x2 += 3
        if pressed[pygame.K_d]: x2 -= 3

    if player1.colliderect(player3):
        x1=30
        y1=30

    if player2.colliderect(player3):
            x2=1000
            y2=30

    screen.blit(Title, (9, 8))

    pygame.display.flip()
    clock.tick(130)