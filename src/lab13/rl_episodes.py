'''
Lab 13: My first AI agent.
In this lab, you will create your first AI agent.
You will use the run_episode function from lab 12 to run a number of episodes
and collect the returns for each state-action pair.
Then you will use the returns to calculate the action values for each state-action pair.
Finally, you will use the action values to calculate the optimal policy.
You will then test the optimal policy to see how well it performs.

Sidebar-
If you reward every action you may end up in a situation where the agent
will always choose the action that gives the highest reward. Ironically,
this may lead to the agent losing the game.
'''
import sys
from pathlib import Path

# line taken from turn_combat.py
sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.pygame_combat import PyGameComputerCombatPlayer
from lab11.turn_combat import CombatPlayer
from lab12.episode import run_episode
from lab11.pygame_ai_player import PyGameAICombatPlayer
from lab12.episode import pygame_combat

from collections import defaultdict
import random
import numpy as np


class PyGameRandomCombatPlayer(PyGameComputerCombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        self.weapon = random.randint(0, 2)
        return self.weapon


class PyGamePolicyCombatPlayer(CombatPlayer):
    def __init__(self, name, policy):
        super().__init__(name)
        self.policy = policy

    def weapon_selecting_strategy(self):
        self.weapon = self.policy[self.current_env_state]
        return self.weapon


def run_random_episode(player, opponent):
    player.health = random.choice(range(10, 110, 10))
    opponent.health = random.choice(range(10, 110, 10))
    return run_episode(player, opponent)


def get_history_returns(history):
    total_return = sum([reward for _, _, reward in history])
    returns = {}
    for i, (state, action, reward) in enumerate(history):
        if state not in returns:
            returns[state] = {}
        returns[state][action] = total_return - sum(
            [reward for _, _, reward in history[:i]]
        )
    return returns


def run_episodes(n_episodes):
    ''' Run 'n_episodes' random episodes and return the action values for each state-action pair.
        Action values are calculated as the average return for each state-action pair over the 'n_episodes' episodes.
        Use the get_history_returns function to get the returns for each state-action pair in each episode.
        Collect the returns for each state-action pair in a dictionary of dictionaries where the keys are states and
            the values are dictionaries of actions and their returns.
        After all episodes have been run, calculate the average return for each state-action pair.
        Return the action values as a dictionary of dictionaries where the keys are states and 
            the values are dictionaries of actions and their values.
    '''
    action_values = {}

    names = ["Legolas", "Saruman"]
    for i in range(n_episodes):
        player = PyGameRandomCombatPlayer("Ira")
        opp = pygame_combat.PyGameComputerCombatPlayer("Computer")
        ep_return = run_random_episode(player, opp)
        history = get_history_returns(ep_return)

        #retrieve all states in returned history

        stateList = list(history.keys())
        splitList = list(history.values())

        # Create the desired dictionary and fill in with the correct information
        # go through all of the states taken from the history dictionary
        for state in stateList:
            # if the state is not in the dictionary yet, create empty dictionary for it
            if state not in action_values:
                action_values[state] = {}
            # each action result is contained in a dictionary, dic
            for dic in splitList:
                # there can be more than one action/result in the dictionary
                for key in dic.keys():
                    # if the state with that action is not created yet, create it
                    if key not in action_values[state]:
                        action_values[state][key] = []
                    action_values[state][key].append(dic[key])

        # Average all of the results for every state-action pair


        print(splitList)
        '''
            if state not in action_values:
                action_values[state] = {}

            for action in history[state]:

                if action not in action_values[state]:
                    action_values[state][action] = {}

                resultList = list((action_values[state][action]).values())
                
                print(resultList)
                #action_values[state][action].update(history[state][action])
        '''
        
        '''
        state_action = {
            state_1 = { 
                action_1: 1, 2, 1, 3, 5}
                action_2{ 2, 4, 1, 2, 2}
            }
            state_2 = { 
                action_1{ 1, 2, 1, 3, 5}
                action_2{ 2, 4, 1, 2, 2}
            }
        }
        numbers in the action dictionaries are the rewards that were given for the specific state-action pair
        '''

    for state in action_values:
        for action in action_values[state]:
            listLength = len(action_values[state][action])
            sumList = sum(action_values[state][action])
            average = sumList/listLength
            action_values[state][action] = average
    return action_values


def get_optimal_policy(action_values):
    optimal_policy = defaultdict(int)
    for state in action_values:
        optimal_policy[state] = max(action_values[state], key=action_values[state].get)
    return optimal_policy


def test_policy(policy):
    names = ["Legolas", "Saruman"]
    total_reward = 0
    for _ in range(100):
        player1 = PyGamePolicyCombatPlayer(names[0], policy)
        player2 = PyGameComputerCombatPlayer(names[1])
        players = [player1, player2]
        total_reward += sum(
            [reward for _, _, reward in run_episode(*players)]
        )
    return total_reward / 100


if __name__ == "__main__":
    #too many runs to do rn, 10000
    action_values = run_episodes(10000)
    print(action_values)
    optimal_policy = get_optimal_policy(action_values)
    print(optimal_policy)
    print(test_policy(optimal_policy))
