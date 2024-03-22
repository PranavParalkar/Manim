import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Nokia Game bana raha hu')
clock = pygame.time.Clock()

# bouncing mechanism variables
jumping = False
gravity_y = 1
jump_height = 20
velocity_y = jump_height
ball_img = pygame.image.load('images/ballimg.png')
player_position = pygame.Vector2(10,290)
dt = 0
angle = 0


# Game Over
win_font = pygame.font.Font('freesansbold.ttf', 128)


#define game variables
tile_size = 50


#load images
bg_img = pygame.image.load('images/background.jpg')

def draw_grid():
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))


def game_win_text():
    win_text = win_font.render("YOU WIN!", True, (255, 255, 255))
    screen.blit(win_text, (220,200))




class World():
	def __init__(self, data):
		self.tile_list = []

		#load images
		dirt_img = pygame.image.load('images/dirt.png')
		grass_img = pygame.image.load('images/dirt_grass.png')
		home_img = pygame.image.load('images/home.png')
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 5:
					img = pygame.transform.scale(home_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])



world_data = [
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5],
[2, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2, 2, 2, 2, 2, -1, 2, 2, 2, 2],
[1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1],
[1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1],
[1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1],
[1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1]


]




world = World(world_data)
run = True
while run:
    dt = clock.tick(60) / 1000  
    screen.blit(bg_img, (0, 0))


    world.draw()
    screen.blit(ball_img,player_position)
    # draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position.x -= 300 * dt

    if keys[pygame.K_RIGHT]: 
        player_position.x += 300 *dt
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        jumping = True
    if keys[pygame.K_q]:
        pygame.quit()
    
    if jumping:
        player_position.y -= velocity_y
        velocity_y -= gravity_y
        if velocity_y < -jump_height:
            jumping = False
            velocity_y = jump_height
    if player_position.x >= screen_width:
    	game_win_text()

    pygame.display.update()

pygame.quit()
