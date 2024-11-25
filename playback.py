import pygame
from game.game_env import Game_Env

# Initialize Pygame
pygame.init()

# Set up the Pygame display
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Connect Four Game Playback')

# Function to display the visualized game state in Pygame
def show_game_state(image):
    # Convert the Pillow image to a Pygame surface
    pygame_image = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
    
    # Display the image on the Pygame window
    screen.blit(pygame_image, (0, 0))
    pygame.display.flip()

# Function to display the winner at the end of the game
def display_winner(winner_text):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(winner_text, True, (0, 0, 0))
    screen.blit(text_surface, (screen_width // 2 - text_surface.get_width() // 2, screen_height - 50))
    pygame.display.flip()

def playback_game(file_path):
    # Initialize the game environment
    env = Game_Env()
    
    # Open the file containing the recorded game actions
    with open(file_path, "r") as f:
        # Read the actions string
        actions_line = f.readline().strip()  # e.g., "0000005345546363421613"
        
        # Read the winner line (e.g., "Player2 Wins")
        winner_text = f.readline().strip()  # e.g., "Player2 Wins"
        
        # Simulate the game by processing each action in the string
        for action in actions_line:
            column = int(action)  # Convert the character to an integer
            env.step(column)  # Simulate dropping a token in the selected column
            
            # Get the visualized game state
            image = env.visualize()
            
            # Show the current game state in Pygame
            show_game_state(image)
            
            # Pause between turns (e.g., 1000 milliseconds = 1 second)
            pygame.time.wait(650)
            
            # Check for quit event (if user closes the window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        
        # After the game ends, display the winner
        display_winner(winner_text)
        
        # Wait for a moment to display the winner before closing
        pygame.time.wait(3000)

# Main execution
file_path = input('Enter the file name of the recorded game: ')
playback_game(file_path)

# Quit Pygame when done
pygame.quit()
