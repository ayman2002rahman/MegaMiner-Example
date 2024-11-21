from game_env import Game_Env

env = Game_Env()
# env.step(0)
env.step(5)
# env.step(4)
# env.step(4)

state = env.get_state()
print(state[1])
Game_Env.visualize(state)
