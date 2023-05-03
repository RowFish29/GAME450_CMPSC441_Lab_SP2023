import sys
import pygame
import random
from os.path import dirname, abspath
import time
from pathlib import Path
from transformers import pipeline
from datetime import datetime

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

from lab11.sprite import Sprite
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes
from lab11.pygame_combat import run_pygame_combat
from lab11.pygame_human_player import PyGameHumanPlayer
from lab11.landscape import get_landscape, get_combat_bg
from lab11.pygame_ai_player import PyGameAIPlayer
from lab7.ga_cities import city_gen
from lab3.travel_cost import get_route_cost, create_route_cooredinates


pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)


def get_landscape_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])


class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes


if __name__ == "__main__":
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "assets/lego.png"
    sprite_speed = 1
    currency = 500

    screen = setup_window(width, height, "Game World Gen Practice")

    landscape_surface = get_landscape_surface(size)
    combat_surface = get_combat_surface(size)
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]

    cities = city_gen(size, len(city_names))
    routesAll = get_routes(cities)
    routes = routesAll
    random.shuffle(routes)
    routes = routes[:10]

    #get route coordinates for travel costs
    route_coordinates = create_route_cooredinates(cities, city_names, routesAll)

    city9connected = False
    routescity9 = []
    city0connected = False
    routescity0 = []

    #if the beginning and/or end city are not connected, find all stored routes and chose one to be
    #connected in the map
    for route in routes:
        if (city9connected == False) & (cities[9] in route):
            city9connected = True
        if (city0connected == False) & (cities[0] in route):
            city0connected = True
    if (city9connected == False  | city0connected == False):
        for allroutes in routesAll:
            if (city9connected == False) & (cities[9] in allroutes):
                routescity9.append(allroutes)
            if (city0connected == False) & (cities[0] in allroutes):
                routescity0.append(allroutes)
        if(city0connected == False):
            route0 = routescity0[random.randint(routescity0.__len__()-1)]
            routes.append(route0)
        if(city9connected == False):
            route9 = routescity9[random.randint(routescity9.__len__()-1)]
            routes.append(route9)



    player_sprite = Sprite(sprite_path, cities[start_city])

    player = PyGameHumanPlayer()


    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=cities,
        routes=routes,
    )
    
    """ Add a line below that will reset the player variable to 
    a new object of PyGameAIPlayer class."""
    player = PyGameAIPlayer(state)

    #begin journal entry
    file = open("src\lab14_final\Journal.txt", "a")
    file.write("Date: " + str(datetime.now()) + "\n")
    file.close()


    while True:
        time.sleep(.01)
        action = player.selectAction(state)
        if 0 <= int(chr(action)) <= 9:
            if int(chr(action)) != state.current_city and not state.travelling:
                start = cities[state.current_city]
                state.destination_city = int(chr(action))
                destination = cities[state.destination_city]
                player_sprite.set_location(cities[state.current_city])
                state.travelling = True
                # where i would put the route costs so its only subtracted once
                # formatting differs from lab3 to this, overall project done as much as it will get
                print(
                    "Travelling from", state.current_city, "to", state.destination_city
                )

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in cities:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayCityNames(cities, city_names)
        if state.travelling:
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                print('Arrived at', state.destination_city)

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            win_lose = run_pygame_combat(combat_surface, screen, player_sprite)
            state.encounter_event = False
            if(win_lose == -1):
                break
            else:
                currency += 50
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.current_city == end_city:
            print('You have reached the end of the game!')
            file.close()
            break
