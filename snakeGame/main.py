import pygame
import random

# Set up the game window
pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the game variables
snake_position = [250, 250]
snake_body = [[250, 250], [240, 250], [230, 250]]
food_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
food_spawned = True
direction = "RIGHT"
change_to = direction
score = 0

# Set up the game loop
game_over = False
clock = pygame.time.Clock()

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"

    # Update the snake direction
    direction = change_to

    # Move the snake
    snake_position = [snake_position[0] + 10 * (direction == "RIGHT") - 10 * (direction == "LEFT"),
                      snake_position[1] + 10 * (direction == "DOWN") - 10 * (direction == "UP")]

    # Check if the snake collided with the food
    if snake_position == food_position:
        food_spawned = False
        score += 1
        snake_body.append([0, 0])

    # Spawn new food if necessary
    if not food_spawned:
        food_position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        food_spawned = True

    # Draw the game objects
    window.fill(BLACK)
    pygame.draw.rect(window, GREEN, [food_position[0], food_position[1], 10, 10])
    for position in snake_body:
        pygame.draw.rect(window, WHITE, [position[0], position[1], 10, 10])

    # Update the snake body positions
    snake_body = [list(snake_position)] + snake_body[:-1]

    # Check if the snake collided with itself or the wall
    if snake_position[0] < 0 or snake_position[0] > 490 or snake_position[1] < 0 or snake_position[1] > 490:
        game_over = True
    if snake_position in snake_body[1:]:
        game_over = True

    # Update the screen
    pygame.display.update()
    clock.tick(10)

# Quit the game
pygame.quit()
