# Zenva Academy Pygame Project.

# Personally added in a level counter for each time you win. When you lose, the game's 
# level is displayed to show your progress and paused using SLEEP from TIME to allow you
# to better see/read the text.

# Allow access to PYGAME library.
import pygame

# Accessing SLEEP to add a pause to the program to read the text.
from time import sleep


# Set size of screen.
SCREEN_TITLE = 'My First RPG Game'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


# Colors per RGB codes.
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Clock used to update game events and frame rate.
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


class Game:

    # Standard FPS
    TICK_RATE = 60

    
    
    # Initializer for the game class to setup the width, height, and title.
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Create a game window with preset size to display the game.
        self.game_screen = pygame.display.set_mode((width, height))
        # Set the game window color to white.
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))
        
    def run_game_loop(self, speed_level, game_level):
        is_game_over = False
        won_game = False
        direction = 0
        
        
        
        player_character = PlayerHero('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyPlayer('enemy.png', 20, 600, 50, 50)
        # Speed increases as you win/advance in the game.
        enemy_0.SPEED *= speed_level
        # Create another enemy.
        enemy_1 = EnemyPlayer('enemy.png', self.width - 40, 450, 50, 50)
        enemy_1.SPEED *= speed_level
        # Create another enemy.
        enemy_2 = EnemyPlayer('enemy.png', 20, 200, 50, 50)
        enemy_2.SPEED *= speed_level
                
        treasure = GameObject('treasure.png', 375, 50, 50, 50)
        
        # Main game loop that runs till is_game_over = True.
        while not is_game_over:
            # Loop for all events possible: mouse movement + clicks + exit events.
            for event in pygame.event.get():
                # For quit events, this allows an exit from game loop.
                if event.type == pygame.QUIT:
                    is_game_over = True
                # Dectect when key is pressed
                elif event.type == pygame.KEYDOWN:
                    # Move up if up key is pressed.
                    if event.key == pygame.K_UP:
                        direction = 1
                    # Move down if down key is pressed.
                    elif event.key == pygame.K_DOWN:
                        direction = -1 
                # Detect when key is released.
                elif event.type == pygame.KEYUP:
                    # Stop movement when key is no longer pressed.
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            # Update game background to remove ghosting.
            self.game_screen.fill(WHITE_COLOR)
            # Update image onto the background.
            self.game_screen.blit(self.image, (0, 0))

            # Draw the treasure.
            treasure.draw(self.game_screen)
            # Update hero position.
            player_character.move(direction, self.height)
            #Draw the updated hero position.
            player_character.draw(self.game_screen)
            
            # Move and draw the enemy.
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
                       

            # Move and draw more enemies as you win/advance in the game.
            if speed_level > 2:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)

            if speed_level > 4:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)

            # End game if collision between enemies and treasure.
            # Close game if won, restart game loop if won.
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                won_game = False
                text = font.render("You lost on level: %s" % game_level, True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                sleep(1.5)
                break
            # Added collision for each new enemy added.
            elif player_character.detect_collision(enemy_1):
                is_game_over = True
                won_game = False
                text = font.render("You lost on level: %s" % game_level, True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                sleep(1.5)
                break
            # Added collision for each new enemy added.
            elif player_character.detect_collision(enemy_2):
                is_game_over = True
                won_game = False
                text = font.render("You lost on level: %s" % game_level, True, BLACK_COLOR)
                self.game_screen.blit(text, (200, 350))
                pygame.display.update()
                sleep(1.5)
                break
            # Added collision for treasure object to detect when you win.
            elif player_character.detect_collision(treasure):
                is_game_over = True
                won_game = True
                text = font.render('You win!', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                sleep(0.5)
                break

             
                
            # Update all game graphics.        
            pygame.display.update()
            # Tick the clock to update everything within the game.
            clock.tick(self.TICK_RATE)

        # Restart game loop if won saving game's speed/level. Breaks out of game loop if quit/lose.
        if won_game:
            self.run_game_loop(speed_level + 0.5, game_level + 1)
        else:
            return



# Generic game object class to be subclassed by other objects in the game.            
class GameObject:

    #
    def __init__(self, image_path, x, y, width, height):
        # Loading player image file from main folder location + scaling image.
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height)) 

        self.x_pos = x
        self.y_pos = y
        
        self.width = width
        self.height = height

    # Draw the object by blitting it onto the background (game screen).
    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))
        
# Class for player controlled hero.
class PlayerHero(GameObject):
    
    # How many titles the hero moves per second.
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Moving the hero up if direction > 0 and down if < 0.
    def move(self, direction, max_height):
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        # Make sure the character never goes to the bottom of the screen.
        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    # Return False (no collision) if y position and x position do not overlap.
    # Return True x and y positions overlap.
    def detect_collision(self, other_object):
        if self.y_pos > other_object.y_pos + other_object.height:
            return False
        elif self.y_pos + self.height < other_object.y_pos:
            return False
        
        if self.x_pos > other_object.x_pos + other_object.width:
            return False
        elif self.x_pos + self.width < other_object.x_pos:
            return False
        
        return True

class EnemyPlayer(GameObject):
    
    # How many titles the hero moves per second.
    SPEED = 5

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    # Move function will move character right once it hits the far left
    # of the screen & left once it hits the far right of the screen.
    def move(self, max_width):
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED
        
            
pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
# Have to pass back game's speed & level.
new_game.run_game_loop(1, 1)

# Quit pygame and the program.
pygame.quit()
quit()



