import sys
import json

# ONLY CHANGE THIS FUNCTION HERE
def choose_action(state):
    player, grid = state
    return 1

if __name__ == "__main__":
    state = json.loads(sys.stdin.read())
    action = choose_action(state)
    print(action)
