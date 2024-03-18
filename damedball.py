import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

fps = 60
timer = pygame.time.Clock()

# Ball parameters
ball_x = 250
ball_y = 100
ball_radius = 45
ball_color = 'grey'
ball_y_speed = 10
gravity = 0.4
bounce_stop = 0.2

# Main game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Gravity and bounce logic
    ball_y_speed += gravity  # Apply gravity
    ball_y += ball_y_speed  # Update vertical position

    # Bounce if the ball hits the ground
    if ball_y >= HEIGHT - ball_radius:
        ball_y = HEIGHT - ball_radius  # Ensure the ball is exactly at the ground
        ball_y_speed = -ball_y_speed * 0.75  # Reverse and reduce speed

        # Stop bouncing if speed is too low
        if abs(ball_y_speed) < bounce_stop:
            ball_y_speed = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()