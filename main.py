import pygame
import random

pygame.init()

pygame.font.init()
pygame.font.get_init()

size = (width, height) = (1200, 600)
screen = pygame.display.set_mode(size)
speed = [2, 4]
if random.randint(0,1)%2==0 :
    speed[0] = -speed[0]
clock = pygame.time.Clock()
running = True
lost = False
dt = 0

icon = pygame.image.load('favicon.png')
pygame.display.set_caption('Board Ball')
pygame.display.set_icon(icon)

font = pygame.font.SysFont("firacode.ttf", 200)
text = font.render("GAME OVER", True, "red")
textrect = text.get_rect()
textrect.center = (screen.get_width() / 2, screen.get_height() / 2)

ball = pygame.Rect(random.uniform(10, width-10), 0, 20, 20)

# board_pos = [screen.get_width() / 2, screen.get_height() * 0.75]
board_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() - 5)
board = pygame.Rect(board_pos.x, board_pos.y, 100, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("violet")
    if not lost:
        board = pygame.Rect(board_pos.x, board_pos.y, 100, 20)
        # ball movement and collision with walls
        ball = ball.move(speed)
        if ball.left < 0 or ball.right > width:
            speed[0] = -speed[0]
        if ball.top < 0:
            speed[1] = -speed[1]
        if ball.bottom >= height:
            lost = True

        # board movement by player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            if board.left > 0:
                board_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            if board.right < width :
                board_pos.x += 300 * dt

        # ball board collision:
        if board.colliderect(ball):
            speed[1] = -speed[1]

        pygame.draw.rect(screen, "red", ball)
        pygame.draw.rect(screen, "red", board)
    else:
        screen.blit(text, textrect)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
