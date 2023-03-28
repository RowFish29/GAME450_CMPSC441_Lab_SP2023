""" Create PyGameAIPlayer class here"""
import random
import pygame
import time
from lab11.turn_combat import CombatPlayer

class PyGameAIPlayer:
    def __init__(self, state) -> None:
        self.last_city = state.cities[state.current_city]
        self.won_game = False

    def selectAction(self, state):
        #check state and routes 
        if(state.travelling == False & self.won_game == False):
            if(state.current_city == 9):
                print("You've Won the Game!")
                self.won_game = True
                return state.current_city

            current_city = state.cities[state.current_city]
            routes = state.routes   
            connect_routes = []
            for position in range(len(routes)):
                #check if a route is connected to the current city
                if(routes[position][0] == current_city):
                    #if(routes[position][1] != self.last_city):
                    connect_routes.append(cityNum(routes[position][1], state))

                if(routes[position][1] == current_city):
                    #if(routes[position][0] != self.last_city):
                    connect_routes.append(cityNum(routes[position][0], state))
            
            if(connect_routes.__len__() == 0):
                return 9
            RandomSelection = random.randint(0, connect_routes.__len__() - 1)

            self.last_city = current_city
            return ord(str(connect_routes[RandomSelection]))
        return ord(str(state.current_city))

def cityNum(travel_city, state):
    TCP = 0
    TP = 0
    for city in state.cities:
        if travel_city == city:
            TCP = TP
            return TCP
        TP = TP + 1

""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        while True:
            time.sleep(.05)
            opp_choice = self.opponent_choices
            if((opp_choice[-1] == 0)):
                self.weapon = 1
                return self.weapon
            if(opp_choice[-1] == 1):
                self.weapon = 2
                return self.weapon
            if(opp_choice[-1] == 2):
                self.weapon = 0
                return self.weapon