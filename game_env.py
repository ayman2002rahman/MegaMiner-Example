action_space = [0, 1, 2, 3, 4, 5, 6, 7] # indices for col positions to drop 
# valid actions may be a subset of action space due to full columns

class Game_Env():
    def __init__(self):
        self.player == 0 # the player whos current turn it is
        self.grid = [[0] * 7] * 6
    
    def get_state(self):
        return self.player, self.grid
    
    def step(self, action):
        
