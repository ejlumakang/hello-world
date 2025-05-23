import sys
from random import randint
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 600, 600

# Define the Grid Dimensions
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define the Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (50, 175, 25)

# Snake Direction
D_RIGHT = (1, 0)
D_LEFT = (-1, 0)
D_UP = (0, -1)
D_DOWN = (0, 1)

def draw_vertical_lines():
    for x in range(0, WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))

def draw_horizontal_lines():
    for y in range(0, HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))

def draw_food(coords):
    pygame.draw.rect(screen, RED, (coords[0] * GRID_SIZE, coords[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_snake(coords_list):
    for coords in coords_list:
        pygame.draw.rect(screen, GREEN, (coords[0] * GRID_SIZE, coords[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def display_score(score):
    score_text = 'Score: ' + str(score)
    font = pygame.font.Font(None, 36)
    score_image = font.render(score_text, True, (0, 0, 0))
    screen.blit(score_image, (0, 0))

def display_game_over():
    game_over_text = 'Game Over!'
    font = pygame.font.Font(None, 70)
    game_over_image = font.render(game_over_text, True, (0, 0, 0))
    text_rect = game_over_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_image, text_rect)

def main():
    # Set up game variables
    clock = pygame.time.Clock()
    is_running = True

    food_coords = (randint(0, 9), randint(0, 9))
    snake_coords_list = [(9, 9), (0, 0)]
    snake_direction = D_RIGHT
    snake_speed = 5
    score = 0

    # Game loop
    while is_running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_direction = D_LEFT
                elif event.key == pygame.K_RIGHT:
                    snake_direction = D_RIGHT
                elif event.key == pygame.K_UP:
                    snake_direction = D_UP
                elif event.key == pygame.K_DOWN:
                    snake_direction = D_DOWN

        # Game logic update
        # Update head location based on direction
        head_x, head_y = snake_coords_list[0]                   
        new_head_x = (head_x + snake_direction[0])
        new_head_y = (head_y + snake_direction[1]) 

        # Collision with apple
        if (new_head_x, new_head_y) == food_coords:
            # Create new food location, update score, increase speed      
            food_coords = (randint(1, 18), randint(1, 18))
            score += 10
            snake_speed += 1
        else:
            # Removes the last tail
            snake_coords_list.pop()

        # Snake steps forward, illusion of a moving snake
        snake_coords_list.insert(0, (new_head_x, new_head_y))  

        # Collision with self and boundaries
        if (new_head_x, new_head_y) in snake_coords_list[1:] or new_head_x < 0 or new_head_x >= GRID_WIDTH or new_head_y < 0 or new_head_y >= GRID_HEIGHT:
            display_game_over()
            pygame.display.flip()
            pygame.time.delay(5000)  
            break

        # Clear the screen
        screen.fill(WHITE)

        # Rendering/Draw
        draw_horizontal_lines()
        draw_vertical_lines()

        # Draw your game elements on the screen here
        draw_food(food_coords)
        draw_snake(snake_coords_list)
        display_score(score)
    
        # Update the display
        pygame.display.flip()

        # Frame rate regulation
        clock.tick(snake_speed)

    # Quit the game properly
    pygame.quit()
    sys.exit()

main()