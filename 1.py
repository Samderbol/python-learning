import pygame
import sys

# Initialize Pygame
pygame.init()

# Set window size
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
bg = (255, 255, 255)

# Create window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monkey Get Banana Animation")

# Load monkey, box, and banana images
MONKEY_IMG = pygame.image.load("monkey.png")
BOX_IMG = pygame.image.load("box.png")
BANANA_IMG = pygame.image.load("banana.png")

# Initial positions for monkey, box, and banana
monkey_x, monkey_y = 1000, 800
box_x, box_y = 200, 800
# Default position parameters assume monkey is to the right of the box

# Recommended values for monkey_x and box_x are between (100, 1000), where larger X values move rightward
banana_x, banana_y = 1000, 200

screen.fill(bg)

# Main animation loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw monkey, box, and banana

    # Update screen
    pygame.display.flip()

    # Control monkey movement
    if monkey_x <= banana_x and box_x != banana_x:
        if monkey_x <= box_x:
            if monkey_x < box_x:
                monkey_x += 1
            elif monkey_x == box_x:
                monkey_x += 1
                box_x += 1
        elif monkey_x >= box_x:
            monkey_x -= 1
            if monkey_x == box_x:
                monkey_x += 1
                box_x += 1
        else:
            monkey_x += 1
            box_x += 1
    else:
        if monkey_x <= banana_x and monkey_y >= banana_y:
            monkey_x += 1
        else:
            if monkey_y >= banana_y - 100:
                monkey_y -= 1
            else:
                monkey_y = banana_y - 100


    screen.blit(MONKEY_IMG, (monkey_x, monkey_y))
    screen.blit(BOX_IMG, (box_x, box_y))
    screen.blit(BANANA_IMG, (banana_x, banana_y))

# Exit animation
pygame.quit()
sys.exit()