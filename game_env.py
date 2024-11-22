import pygame
import sys

action_space = [0, 1, 2, 3, 4, 5, 6, 7] # indices for col positions to drop 
# valid actions may be a subset of action space due to full columns

class Game_Env():
    def __init__(self):
        self.player = 1 # (1 or 2 to represent current player)
        self.stacks = [[] for _ in range(7)]
        self.turns = 0 # number of valid turns made
    
    def reset(self):
        self.player = 1
        self.stacks = [[] for _ in range(7)]

    def get_grid(self):
        grid = [[0] * 7 for _ in range(6)]
        for j, stack in enumerate(self.stacks):
            for i, disk in enumerate(stack):
                grid[5-i][j] = disk
        return grid

    def get_state(self):
        return self.player, self.get_grid()
    
    def visualize(state): # visualize a specific state (this uses pygame)
        pygame.init()

        # Constants
        ROWS, COLS = 6, 7
        CELL_SIZE = 100
        RADIUS = CELL_SIZE // 2 - 10
        WIDTH = COLS * CELL_SIZE
        HEIGHT = (ROWS + 1) * CELL_SIZE  # Extra row for the current player display
        WHITE = (255, 255, 255)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        BLACK = (0, 0, 0)

        # Extract state information
        player, grid = state

        # Initialize screen
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Connect Four")

        def draw_board():
            # Draw the board background
            for row in range(ROWS):
                for col in range(COLS):
                    pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, (row + 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), RADIUS)

            # Draw the pieces on the grid
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 1:
                        pygame.draw.circle(screen, RED, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), RADIUS)
                    elif grid[row][col] == 2:
                        pygame.draw.circle(screen, YELLOW, (col * CELL_SIZE + CELL_SIZE // 2, (row + 1) * CELL_SIZE + CELL_SIZE // 2), RADIUS)

        # Main loop to display the board
        clock = pygame.time.Clock()
        while True:
            screen.fill(WHITE)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Display current player's turn
            font = pygame.font.SysFont("Arial", 36)
            turn_text = f"Player {player}'s Turn"
            text_surface = font.render(turn_text, True, RED if player == 1 else YELLOW)
            screen.blit(text_surface, (10, 10))

            # Draw the board and update the display
            draw_board()
            pygame.display.flip()

            # Limit the frame rate
            clock.tick(30)

    # ==== helper functions to help game logic ====

    def solution(self):
        grid = self.get_grid()
        # horizontal
        for i in range(6):
            for j in range(4):
                for k in range(4):
                    if grid[i][j+k] != self.player:
                        break
                else:
                    return True
        
        # vertical
        for i in range(3):
            for j in range(7):
                for k in range(4):
                    if grid[i+k][j] != self.player:
                        break
                else:
                    return True

        # right diagonal     
        for i in range(3):
            for j in range(4):
                for k in range(4):
                    if grid[i+k][j+k] != self.player:
                        break
                else:
                    return True

        # left diagonal
        for i in range(3):
            for j in range(3, 7):
                for k in range(4):
                    if grid[i+k][j-k] != self.player:
                        break
                else:
                    return True

        return False

    def get_valid_actions(self):
        actions = []
        for j in range(7):
            if len(self.stacks[j]) != 6:
                actions.append(j)
        return actions

    def step(self, action): # --> state, reward, terminated
        # invalid action
        if len(self.stacks[action]) == 6:
            return self.get_state(), -10, False, 'Invalid'
        
        # drop disk
        self.stacks[action].append(self.player)

        # check if won
        if self.solution():
            win_string = 'Player1 Wins' if self.player == 1 else 'Player2 Wins'
            return self.get_state(), 10, True, win_string
        
        self.player = 2 if self.player == 1 else 1
        disks = 0
        for stack in self.stacks:
            disks += len(stack)
        if disks == 42:
            return self.get_state(), 0, True, 'Stalemate'
        return self.get_state(), 0, disks == 42, ''
    
        
