# from game_env import Game_Env
# from ai1 import 

# env = Game_Env()

# this could prob be done best with a scrip file that runs ai1.py and ai2.py altertating
# pass in 
# the functions inside this should take in current 

# competitors will only write one function to submit:
# ai(env) --> action
# the game runer will then use this action to perform out the game


# people using RL will also need to define their own reward function
# reward function will need to be defined as 
# reward(state, state_prime) --> reward
# only intested in what has changed in the state of the game, then you can write code to check state attribute diferences and determine positive and negativer values for reward

# for players using RL, in order to train, they make steps in the eviornment and 

from game_env import Game_Env

env = Game_Env()