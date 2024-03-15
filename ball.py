from moderngl_window.context.base import window
import pygame
from pygame.draw import circle

stat = pygame.init()

#print(stat)

window_1 = pygame.display.set_mode((500,500)) 
clock_bhai = pygame.time.Clock()
dt = 0
speed = pygame.Vector2(0,10)
running = True

player_position = pygame.Vector2(window_1.get_width()/2,window_1.get_width()/2)

while running:
	window_1.fill("black")
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	player_position += speed * dt

	gola = pygame.draw.circle(window_1,"white",player_position,50)

	if player_position.y >= window_1.get_height() - 50 :
		speed = -speed
	

	pygame.display.flip()
	dt = clock_bhai.tick(60) / 100
	print(dt)

pygame.quit()