import pygame
pygame.init()

size = (width, height) = (1280, 720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
running = True

ball = pygame.Rect(0, 0, 20, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("violet")
    pygame.draw.rect(screen, "red", ball)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()