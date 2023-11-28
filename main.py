import pygame

pygame.init()

size = (width, height) = (1200, 600)
screen = pygame.display.set_mode(size)
speed = [2, 2]
clock = pygame.time.Clock()
running = True
dt = 0

ball = pygame.Rect(0, 0, 20, 20)

# board_pos = [screen.get_width() / 2, screen.get_height() * 0.75]
board_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() * 0.75)
board = pygame.Rect(board_pos.x, board_pos.y, 100, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("violet")
    board = pygame.Rect(board_pos.x, board_pos.y, 100, 20)
    # ball movement and collision with walls
    ball = ball.move(speed)
    if ball.left < 0 or ball.right > width:
        speed[0] = -speed[0]
    if ball.top < 0 or ball.bottom > height:
        speed[1] = -speed[1]

    # board movement by player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        board_pos.y -= 300 * dt
    if keys[pygame.K_a]:
        board_pos.x -= 300 * dt
    if keys[pygame.K_s]:
        board_pos.y += 300 * dt
    if keys[pygame.K_d]:
        board_pos.x += 300 * dt

    pygame.draw.rect(screen, "red", ball)
    pygame.draw.rect(screen, "red", board)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
