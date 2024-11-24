from game_env import Game_Env

# this file simulates a past game given its txt file
file_path = input('Enter the file name of the recorded game: ')
env = Game_Env()
f = open(file_path, "r")
for line in f.lines():
    action = int(line.strip())
    env.step(action)
f.close()