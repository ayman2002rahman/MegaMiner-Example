import sys
import json
import os
import random

# file_path = os.path.abspath('../../')
# if file_path not in sys.path:
#     sys.path.append(file_path)
# from game_env import ACTION_SPACE
ACTION_SPACE = [0, 1, 2, 3, 4, 5, 6]

# PUT YOUR IMPORTS HERE
import pickle

# ONLY CHANGE THIS FUNCTION HERE
def choose_action(state):
    player, grid = state
    valid_actions = set()
    for j in range(7):
        if grid[0][j] == 0:
            valid_actions.add(j)

    def hash_state(state): # make state tuple hashable
        hashed_grid = tuple(tuple(row) for row in state[1])
        return (state[0], hashed_grid)
    
    state = hash_state(state)
    with open('./ai/team1/qtable.pkl', 'rb') as file:
        Qtable = pickle.load(file)

    def get_q_value(Qtable, state, action):
        return Qtable.get((state, action), 0.0)

    def get_max(Qtable, state):
        best_action = None
        max_q_value = float('-inf')
        for action in ACTION_SPACE:
            q_value = get_q_value(Qtable, state, action)
            if q_value > max_q_value:
                max_q_value = q_value
                best_action = action
        return max_q_value, best_action

    def greedy_policy(Qtable, state):
        return get_max(Qtable, state)[1]

    action = greedy_policy(Qtable, state)
    if action not in valid_actions:
        return random.choice(list(valid_actions))
    return action

if __name__ == "__main__":
    state = json.loads(sys.stdin.read())
    action = choose_action(state)
    print(action)
