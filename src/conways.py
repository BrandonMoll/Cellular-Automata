import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
BLUE = (0, 0, 255)
WIN_SIZE = 500
WIDTH_SIZE = 600

cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
next_states = [0] * 400
generation = 0
# for i in range(400):
#     roll = random.randint(0, 10)
#     if roll < 1:
#         cur_states[i] = 1

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIDTH_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
#Buttons
pause_button = pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 100, 50))
 
# Loop until the user clicks the close button.
done = False
paused = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    if event.type == pygame.MOUSEBUTTONDOWN:         
        click_pos = pygame.mouse.get_pos()  
        print(click_pos)     
        if pause_button.collidepoint(click_pos):        
            paused = not paused

    def check_neighbors(current, index):
        alive_neighbors = 0
        if index == 0:
            if current[index + 20] == 1:
                alive_neighbors += 1

            if current[index + 1] == 1:
                alive_neighbors += 1

            if current[index + 21] == 1:
                alive_neighbors += 1
        elif index == 19:
            if current[index + 20] == 1:
                alive_neighbors += 1

            if current[index - 1] == 1:
                alive_neighbors += 1

            if current[index + 19] == 1:
                alive_neighbors += 1
        elif index == 380:
            if current[index - 20] == 1:
                alive_neighbors += 1

            if current[index + 1] == 1:
                alive_neighbors += 1

            if current[index - 19] == 1:
                alive_neighbors += 1
        elif index == 399:
            if current[index - 20] == 1:
                alive_neighbors += 1

            if current[index - 1] == 1:
                alive_neighbors += 1

            if current[index - 21] == 1:
                alive_neighbors += 1
        elif index % 20 == 0:
            if current[index - 20] == 1:
                alive_neighbors += 1

            if current[index + 20] == 1:
                alive_neighbors += 1

            if current[index - 19] == 1:
                alive_neighbors += 1

            if current[index + 1] == 1:
                alive_neighbors += 1

            if current[index + 21] == 1:
                alive_neighbors += 1
        elif (index + 1) % 20 == 0:
            if current[index - 20] == 1:
                alive_neighbors += 1

            if current[index + 20] == 1:
                alive_neighbors += 1

            if current[index - 21] == 1:
                alive_neighbors += 1

            if current[index - 1] == 1:
                alive_neighbors += 1

            if current[index + 19] == 1:
                alive_neighbors += 1
        elif index - 19 <= 0:
            if current[index - 1] == 1:
                alive_neighbors += 1

            if current[index + 1] == 1:
                alive_neighbors += 1

            if current[index + 19] == 1:
                alive_neighbors += 1

            if current[index + 20] == 1:
                alive_neighbors += 1

            if current[index + 21] == 1:
                alive_neighbors += 1
        elif index + 19 >= 400:
            if current[index - 1] == 1:
                alive_neighbors += 1

            if current[index + 1] == 1:
                alive_neighbors += 1

            if current[index - 19] == 1:
                alive_neighbors += 1

            if current[index - 20] == 1:
                alive_neighbors += 1

            if current[index - 21] == 1:
                alive_neighbors += 1
        else:
            if current[index + 1] == 1:
                alive_neighbors += 1

            if current[index - 1] == 1:
                alive_neighbors += 1

            if current[index + 20] == 1:
                alive_neighbors += 1

            if current[index - 20] == 1:
                alive_neighbors += 1

            if current[index + 21] == 1:
                alive_neighbors += 1

            if current[index - 21] == 1:
                alive_neighbors += 1

            if current[index + 19] == 1:
                alive_neighbors += 1

            if current[index - 19] == 1:
                alive_neighbors += 1

        if current[index] == 0:
            if alive_neighbors >= 3:
                return 1
            else:
                return 0
        else:
            if alive_neighbors == 2 or alive_neighbors == 3:
                return 1
            elif alive_neighbors >= 4:
                return 0
            elif alive_neighbors <= 1:
                return 0


    
    if not paused:
        for i in range(len(cur_states)):
            next_states[i] = check_neighbors(cur_states, i)

        generation += 1
    
    pygame.display.set_caption(f'Conway\'s Game of Life, Generation: {generation}')

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 100, 50))
    cur_index = 0
    x = 103
    while x < 600:
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
    if not paused:
        for i in range(len(cur_states)):
            cur_states[i] = next_states[i]


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
