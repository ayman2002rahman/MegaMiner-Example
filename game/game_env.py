import sys
from PIL import Image, ImageDraw, ImageFont

# Game constants
ACTION_SPACE = [0, 1, 2, 3, 4, 5, 6] # indices for col positions to drop 
ROWS = 6
COLUMNS = 7
# valid actions may be a subset of action space due to full columns

class Game_Env():
    def __init__(self):
        self.player = 1 # (1 or 2 to represent current player)
        self.stacks = [[] for _ in range(7)]
        self.turns = 0 # number of valid turns made
    
    def reset(self):
        self.player = 1
        self.stacks = [[] for _ in range(7)]
        return self.get_state(), 'Game Start'

    def get_grid(self):
        grid = [[0] * 7 for _ in range(6)]
        for j, stack in enumerate(self.stacks):
            for i, disk in enumerate(stack):
                grid[5-i][j] = disk
        return grid

    def get_state(self):
        return self.player, self.get_grid()
    
    def visualize(self):
        # Canvas dimensions
        canvas_width = 700
        canvas_height = 600
        cell_size = 100  # Size of each grid cell (100x100 pixels)
        
        # Create a blank image (white canvas)
        image = Image.new('RGB', (canvas_width, canvas_height), color='white')
        
        # Create a drawing context
        draw = ImageDraw.Draw(image)
        
        # Colors for the players' tokens
        player1_color = (255, 0, 0)  # Red for player 1
        player2_color = (255, 255, 0)  # Yellow for player 2
        empty_color = (200, 200, 200)  # Light grey for empty spaces
        
        # Draw the Connect Four grid (7 columns, 6 rows)
        for row in range(6):
            for col in range(7):
                # Calculate the position of the top-left corner of each cell
                x0 = col * cell_size
                y0 = row * cell_size + 50  # Offset to leave space for the "Turn" text
                x1 = x0 + cell_size
                y1 = y0 + cell_size
                
                # Draw the empty grid background
                draw.rectangle([x0, y0, x1, y1], outline='black', fill=empty_color)
                
                # Draw the token in the column if there are any
                if len(self.stacks[col]) > row:
                    token = self.stacks[col][row]
                    if token == 1:
                        draw.ellipse([x0 + 10, y0 + 10, x1 - 10, y1 - 10], fill=player1_color)
                    elif token == 2:
                        draw.ellipse([x0 + 10, y0 + 10, x1 - 10, y1 - 10], fill=player2_color)
        
        # Draw the current player's turn at the top
        font = ImageFont.load_default()
        turn_text = f"Player {self.player}'s Turn"
        draw.text((canvas_width // 2 - 60, 10), turn_text, fill='black', font=font)
        
        return image


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

    def step(self, action): # --> state, reward, terminated, result
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
    
        
