import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
next_states = [0] * 400

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    def check_neighbors(current, index):
        dead_neighbors = []
        alive_neighbors = []
        if index == 0:
            if current[index + 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        elif index == 19:
            if current[index + 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        elif index == 380:
            if current[index - 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        elif index == 399:
            if current[index - 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        elif index % 20 == 0:
            if current[index - 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        elif (index + 1) % 20 == 0:
            if current[index - 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        elif index - 19 <= 0:
            if current[index - 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        elif index + 19 >= 400:
            if current[index - 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)
        else:
            if current[index + 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 1] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 20] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 21] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index + 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

            if current[index - 19] == 0:
                dead_neighbors.append(0)
            else:
                alive_neighbors.append(1)

        if current[index] == 0:
            if len(alive_neighbors) >= 3:
                return 1
            else:
                return 0
        else:
            if len(alive_neighbors) == 2 or len(alive_neighbors) == 3:
                return 1
            elif len(alive_neighbors) >= 4:
                return 0
            elif len(alive_neighbors) <= 1:
                return 0

    for i in range(len(cur_states)):
        next_states[i] = check_neighbors(cur_states, i)






 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    cur_index = 0
    x = 3
    while x < 500:
        y = 3
        while y < 500:
            state = cur_states[cur_index]
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
            cur_index += 1
            y += 25
        x += 25
    
        cur_states = next_states

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(1)
 
# Close the window and quit.
pygame.quit()
