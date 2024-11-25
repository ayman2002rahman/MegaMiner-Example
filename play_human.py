from game.game_env import Game_Env

env = Game_Env()
env.step(0)
env.step(5)
env.step(4)
env.step(4)
env.step(4)
env.step(0)
env.step(4)
env.step(0)

state = env.get_state()
print(state[1])
Game_Env.visualize(state)

# this program will need to visualize a diff pygame apart from env.visualize(state) to allow more interactivity and allow clickign controls in the game
# 