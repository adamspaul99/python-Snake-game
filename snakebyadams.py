# First of all we have to download pygame module by using 'pip install pygame' in our terminal.
# Importing pygame module.
import pygame

# Importing random module to print random numbers.
import random

# Importing OS module to creat files
import os

# This will allow us to play music
pygame.mixer.init()


# This will initialse all the modules of pygame module.
x = pygame.init()


# This will generate our window of our desired (width, height).
screen_width = 500
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.update() # There is no need to write this function here because it is automatically udated but for a good practice we write this function.


# This will set the title of our game.
pygame.display.set_caption("Snakes with AdamsPaul")

# Colors which are going to use throughout the code
white = (255, 255, 255) # Colour according to there RGB value
red = (255, 0, 0) # Colour according to there RGB value
black = (0, 0, 0) # Colour according to there RGB value

fps = 60 # Frame rate per second
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25) # Choosing font.


# The below function will print score on screen.
def textOnScreen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# The below function will plot our snake in game window.
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, (x, y, snake_size, snake_size))

# The below loop is welcome loop, i.e. first screen after we open our game.
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((133,153,172))
        textOnScreen("Welcome to the snake game..........", black, 110, 150)
        textOnScreen("Use arrow keys to move.", black, 140, 175)
        textOnScreen("Press 'Space Bar' to play the game.", black, 116, 440)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        pygame.display.update()
        clock.tick(fps)


# Creating a gmae loop
def game():
    # Game specific variables
    
    
    exit_game = False  # exit_game variable is use to  quit our game when it will become True.
    game_over = False  # game_over variable is use to to handle game over event, it will become True when game is over.
    snake_x = 45  # Initial position of snake in x-Axis
    snake_y = 45 # Initial position of snake in y-Axis
    snake_size = 10 # Initial size of snake
    

    velocity = 2.6 # velocity of snake
    velocity_x = 0 # This will give velocity in x-axis
    velocity_y = 0 # This will give velocity in y-axis

    food_x = random.randint(35, 450) # This will generate snake food at random Co-ordinates
    food_y = random.randint(35, 450) # This will generate snake food at random Co-ordinates
    food_size = 8 # It defines food size

    snake_list = []
    snake_len = 1

    score = 0

    # Check if highscore.txt file exists.
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()
    

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # This will handle quit game event.
                        exit_game = True

                if event.type == pygame.KEYDOWN: # Detects any key pressed or not.
                        if event.key == pygame.K_RETURN: # This will restart our game.
                            welcome()

            gameWindow.fill(white)
            textOnScreen("GAME OVER!!!!!    Sanke Dead", red, 128, 210)
            textOnScreen("Now press 'Enter' to continue", red, 132, 235)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # This will handle quit game event.
                    exit_game = True
                
                if event.type == pygame.KEYDOWN: # Detects any key pressed or not.
                    if event.key == pygame.K_RIGHT: # Detects right arrow key pressed or not.
                        velocity_x = velocity # Moves right
                        velocity_y = 0

                    if event.key == pygame.K_LEFT: # Detects left arrow key pressed or not.
                        velocity_x = -velocity # Moves left
                        velocity_y = 0

                    if event.key == pygame.K_UP: # Detects up arrow key pressed or not.
                        velocity_y = -velocity # Moves up
                        velocity_x = 0

                    if event.key == pygame.K_DOWN: # Detects down arrow key pressed or not.
                        velocity_y = velocity # Moves down
                        velocity_x = 0

                    # The below slice of code is cheat code.
                    if event.key == pygame.K_y: # Detects down arrow key pressed or not.
                        score = score + 10 

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score = score + 10
                if score > int(highscore):
                    highscore = score
                
                food_x = random.randint(40, 450)
                food_y = random.randint(40, 450)

                snake_len = snake_len + 4

            gameWindow.fill(white) # This will set background colour white.

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_len: # This will maintain sanke length.
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('khatam.mp3')
                pygame.mixer.music.play()


            textOnScreen("Score: " + str(score) + "                               High Score: " + str(highscore), red, 10, 10) # This will print Score.

            line = pygame.draw.line(gameWindow, black, (500, 33), (00, 33)) # This will draw a horizontal line.

            # Below if statement will handle game over.
            if snake_x < 0 or snake_y < 33 or snake_x > screen_width or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('khatam.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snake_list, snake_size) # This will make snake head and its initial postiton.
            
            pygame.draw.rect(gameWindow, red, pygame.Rect(food_x, food_y, food_size, food_size))  # This will make snake food at random postiton.


        pygame.display.update() # For update all changes in display.
        clock.tick(fps)


    # After game loop exits, below two functions will run.
    pygame.quit()
    quit()
welcome()
game()