import pygame
import math 

pygame.init()

WIDTH, HEIGHT = 1000,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slingshot ball")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Constants
FPS = 60
GRAVITY = 0.5

# Slingshot Properties
slingshot_pos = (200, HEIGHT - 100)
slingshot_radius = 20
pull_back_length = 100

# Ball Properties
ball_radius = 15
ball_color = RED
ball_pos = slingshot_pos
ball_velocity = [0, 0]  # Initialize ball velocity

# Slingshot mechanics variables
is_pulling_back = False
pull_back_distance = 0
angle = 0

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_pulling_back = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_pulling_back = False
                ball_speed = min(pull_back_distance, pull_back_length)
                angle_radians = math.radians(angle)
                ball_velocity[0] = (ball_speed * math.cos(angle_radians))
                ball_velocity[1] = (-ball_speed * math.sin(angle_radians))

    gola = pygame.draw.circle(screen, RED, slingshot_pos, 50)

    if is_pulling_back:
        mouse_pos = pygame.mouse.get_pos()
        pull_back_distance = min(pull_back_length, math.dist(slingshot_pos, mouse_pos))
        angle = math.degrees(math.atan2(slingshot_pos[1] - mouse_pos[1], slingshot_pos[0] - mouse_pos[0]))
        pygame.draw.line(screen,BLACK,slingshot_pos,mouse_pos,2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
