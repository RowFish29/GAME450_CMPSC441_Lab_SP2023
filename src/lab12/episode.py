
import sys
from pathlib import Path
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))
from lab11.pygame_ai_player import PyGameAICombatPlayer
from lab11 import pygame_combat
''' 
Lab 12: Beginnings of Reinforcement Learning
We will modularize the code in pygrame_combat.py from lab 11 together.

Then it's your turn!
Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''

def run_episode(player, opponent):
    #get all actions from the current game
    current_game = pygame_combat.Combat()
    GameState = []
    while not current_game.gameOver:
        reward = pygame_combat.run_turn(current_game, player=player, opponent=opponent)
        observation = (player.health, opponent.health)
        GameState.append([observation, player.weapon, reward])

    return GameState

    # return tuple (observation/state, action, reward)
    #   observation/state -> tuple of (player1_health, player2_health)
    #   action -> weapon selected by player
    #   reward -> what player gets for that turn

if __name__ == "__main__":
    player = PyGameAICombatPlayer("Ira")
    opp = pygame_combat.PyGameComputerCombatPlayer("Computer")
    print(run_episode(player, opp))
