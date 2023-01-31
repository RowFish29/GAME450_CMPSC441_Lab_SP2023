'''
Lab 4: Rock-Paper-Scissor AI Agent

In this lab you will build one AI agent for the game of Rock-Paper-Scissors, that can defeat a few different kinds of 
computer players.

You will update the AI agent class to create your first AI agent for this course.
Use the precept sequence to find out which opponent agent you are facing, 
so that it can beat these three opponent agents:

    Agent Single:  this agent picks a weapon at random at the start, 
                   and always plays that weapon.  
                   For example: 2,2,2,2,2,2,2,.....

    Agent Switch:  this agent picks a weapon at random at the start,
                   and randomly picks a weapon once every 10 rounds.  
                   For example:  2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,...

    Agent Mimic:  this agent picks a weapon at random in the first round, 
                  and then always does what you did the previous round.  
                  For example:  if you played 1,2,0,1,2,0,1,2,0,...  
                   then this agent would play 0,1,2,0,1,2,0,1,2,...

Discussions in lab:  You don't know ahead of time which opponent you will be facing, 
so the first few rounds will be used to figure this out.   How?

Once you've figured out the opponent, apply rules against that opponent. 
A model-based reflex agent uses rules (determined by its human creator) to decide which action to take.

If your AI is totally random, you should be expected to win about 33% of the time, so here is the requirement:  
In 100 rounds, you should consistently win at least 85 rounds to be considered a winner.

You get a 1 point for beating the single agent, 2 points for beating the switch agent, 
and 2 points for beating the mimic agent.

'''
# we write a class that wins against the 3 players no matter what agent we are facing

from rock_paper_scissor import Player
from rock_paper_scissor import run_game
from rock_paper_scissor import random_weapon_select

class AiPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.initial_weapon = random_weapon_select()
    
    def weapon_selecting_strategy(self):
        #single always chooses same 
        #switch changes every 10 rounds
        #Mimic follows suit
        #rock, paper, scissors
        #0, 1, 2
        #rock v paper = paper (0, 1, 1)
        #paper v scissors = scissors (1, 2, 2)
        #scissors v rock = rock (2, 0, 0)

        #if this is the first move
        if len(self.opponent_choices) == 0:
            return self.initial_weapon
        
        if(len(self.my_choices) > 1):
            #if the players last move was chosen, then its likely a mimic
            #Test 1 - Final tally:  [99.33676767676765, 93.22533293143336, 99.30000000000003]
            #Test 2 - Final tally:  [99.33696969696962, 93.2456084503933, 99.34000000000003]
            #Test 3 - Final tally:  [99.27575757575752, 93.22510121617613, 99.20000000000002]
            if((self.my_choices[-2] == self.opponent_choices[-1])):
                #use the last decision made to beat the mimic
                if(self.my_choices[-1] == 2):
                    return 0
                else:
                    return self.my_choices[-1] + 1

        return (self.opponent_choices[-1]+1)%3
        pass



if __name__ == '__main__':
    final_tally = [0]*3
    for agent in range(3):
        #do 50 rounds rn instead
        for i in range(100):
            tally = [score for _, score in run_game(AiPlayer("AI"), 100, agent)]
            if sum(tally) == 0:
                final_tally[agent] = 0
            else:
                final_tally[agent] += tally[0]/sum(tally)

    print("Final tally: ", final_tally)  