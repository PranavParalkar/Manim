from moderngl_window.context.base import keys, window
import pygame
from pygame.draw import circle

stat = pygame.init()

#print(stat)

window_1 = pygame.display.set_mode((500,500)) 
clock_bhai = pygame.time.Clock()
dt = 0
speed = pygame.Vector2(0,10)
running = True
circle_radius = 40 

player_position = pygame.Vector2(window_1.get_width()/2,window_1.get_width()/2)

while running:
    window_1.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gola = pygame.draw.circle(window_1,"white",player_position,40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_position.y -= 300 *dt
    if keys[pygame.K_s]:
        player_position.y += 300 *dt
    if keys[pygame.K_a]:
        player_position.x -= 300 *dt
    if keys[pygame.K_d]:
        player_position.x += 300 *dt
    if keys[pygame.K_q]:
        pygame.quit()

    if player_position.x >= (window_1.get_width() + (circle_radius)):
        player_position.x = 0 - circle_radius
    if player_position.y >= (window_1.get_height() + (circle_radius)):
        player_position.y = 0 - circle_radius
    
    
    pygame.display.flip()
    dt = clock_bhai.tick(60) / 1000
    print(dt)

pygame.quit()
