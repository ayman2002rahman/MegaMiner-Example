import subprocess
import json
from game_env import Game_Env

def get_action(player_script, state):
    # Serialize state to JSON and send it to the external script.
    state_json = json.dumps(state)
    result = subprocess.run(
        player_script,
        input=state_json,
            text=True,
        capture_output=True,
    )
    return int(result.stdout.strip())  # Expect a valid action index.

def run_game(env, player1_script, player2_script, record_file):
    players = [player1_script, player2_script]
    turn = 0
    f = open(record_file, "w")

    terminated = False
    while not terminated:
        current_player = players[turn % 2]
        action = get_action(current_player, env.get_state())
        if action not in env.get_valid_actions():
            raise ValueError(f"Invalid action {action} by player {turn % 2}")
        env.state, _, terminated, game_message = env.step(action)
        f.write(str(action))
        if game_message in ['Player1 Wins', 'Player2 Wins', 'Stalemate']:
            f.write('\n')
            f.write(game_message)
        turn += 1

    f.close()
    return env.get_state()  # Return final game state for evaluation.

env = Game_Env()
run_game(env, ['python3', 'ai1.py'], ['python3', 'ai2.py'], 'record_file.txt')
