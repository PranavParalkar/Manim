# Shubham Pawade

import pygame
import math
 
from pygame.cursors import ball
 
pygame.init()
 
WIDTH, HEIGHT = 1000, 800
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SlingShot Ball")
 
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
 
FPS = 60
GRAVITY = 0.5
 
slingshot_pos = (200, HEIGHT -100)
slingshot_radius = 30
pull_back_length = 120
 
ball_radius = 15
ball_color = RED
ball_pos = slingshot_pos
 
is_pulling_back = False
pull_back_distance = 0
angle = 0
 
clock = pygame.time.Clock()
running = True
 
# VELOCITY KB DENI HAI JB BALL RELASE HOGI
# MOUSE KA INITAL AND FINAL DISTANCE KE HISAB SE VELOCITY DENGE
 
while running:
    screen.fill(WHITE)
 
 
 
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                is_pulling_back = True 
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
                is_pulling_back = False
                ball_speed = min(pull_back_distance, pull_back_length) * 0.5
                angle_radians = math.radians(angle)
                ball_velocity = (ball_speed * math.cos(angle_radians), ball_speed * -math.sin(angle_radians))
                ball_pos = (slingshot_pos[0] + pull_back_distance * math.cos(angle_radians), slingshot_pos[1] - pull_back_distance * math.sin(angle_radians))
                pull_back_distance = 0
 
    if is_pulling_back:
        mouse_pos = pygame.mouse.get_pos()
        pull_back_distance = -min((math.sqrt((mouse_pos[0] - slingshot_pos[0]) ** 2 + (mouse_pos[1] - slingshot_pos[1]) **2)), pull_back_length)
        angle = math.degrees(math.atan2(slingshot_pos[1] - mouse_pos[1], mouse_pos[0] - slingshot_pos[0]))
 
    pygame.draw.circle(screen, BLACK, slingshot_pos, slingshot_radius)
 
    pygame.draw.line(screen, BLACK, slingshot_pos, (slingshot_pos[0] + pull_back_distance * math.cos(math.radians(angle)),                                            
                                                    slingshot_pos[1] - pull_back_distance * math.sin(math.radians(angle))),4)
 
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
 
    try:
        ball_pos = (ball_pos[0] + ball_velocity[0], ball_pos[1] + ball_velocity[1])
        ball_velocity = (ball_velocity[0], ball_velocity[1] + GRAVITY)
    except NameError:
        pass
 
    pygame.display.flip()
    clock.tick(50)
 
pygame.quit()
 