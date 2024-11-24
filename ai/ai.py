import sys
import json
import os

file_path = os.path.abspath('../../')
if file_path not in sys.path:
    sys.path.append(file_path)
from game_env import ACTION_SPACE

# PUT YOUR IMPORTS HERE

# ONLY CHANGE THIS FUNCTION HERE
def choose_action(state):
    player, grid = state
    return 0 

if __name__ == "__main__":
    state = json.loads(sys.stdin.read())
    action = choose_action(state)
    print(action)
