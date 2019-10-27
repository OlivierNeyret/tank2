# Copyright (C) 2019 Olivier Neyret

# This file is part of Tank2.

# Tank2 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Tank2 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Tank2.  If not, see <https://www.gnu.org/licenses/>.

from player import Player, Team
from human_player import Human_Player
from ai_player import AI_Player
from rocket import Rocket
import sys
import enum
import pygame
import threading
import time

WIDTH_MAP = 13
HEIGHT_MAP = 12

FREQ_ROCKET = 0.02
DELAY_BASE = 0.5

class Difficulty(enum.Enum):
    NONE = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Game:
    def __init__(self, nb_human_player, nb_ai_player, level):
        self.nb_human_player = nb_human_player
        self.nb_ai_player = nb_ai_player
        self.players = []
        self.rockets = []
        self.base_timers = []
        self.level = level
        for i in range(nb_human_player):
            if i % 2 == 0:
                self.players.append(Human_Player(Team.BLUE))
            else:
                self.players.append(Human_Player(Team.RED))
        for i in range(nb_ai_player):
            if i % 2 == 0:
                self.players.append(AI_Player(Team.BLUE))
            else:
                self.players.append(AI_Player(Team.RED))
        self.map = []
        map_file = open("maps/map"+str(level)+".map", "r")
        for line in map_file:
            if line[-1] == '\n':
                self.map.append(line[:-1]) # Remove last char (i.e. '\n')
            else:
                self.map.append(line)

    def move(self, player, direction):
        if direction == 'down':
            player.orientation = 'S'
            # Check map collision
            if player.pos[1] < HEIGHT_MAP - 1 and self.map[player.pos[1]+1][player.pos[0]] != 'm' and self.map[player.pos[1]+1][player.pos[0]] != '%' and self.map[player.pos[1]+1][player.pos[0]] != '$':
                # Check player collision
                for other_player in self.players:
                    if player != other_player:
                        if other_player.pos[0] == player.pos[0] and other_player.pos[1] == player.pos[1] + 1:
                            return
                player.pos[1] += 1
        elif direction == 'up':
            player.orientation = 'N'
            # Check map collision
            if player.pos[1] > 0 and self.map[player.pos[1]-1][player.pos[0]] != 'm' and self.map[player.pos[1]-1][player.pos[0]] != '%' and self.map[player.pos[1]-1][player.pos[0]] != '$':
                # Check player collision
                for other_player in self.players:
                    if player != other_player:
                        if other_player.pos[0] == player.pos[0] and other_player.pos[1] == player.pos[1] - 1:
                            return
                player.pos[1] -= 1
        elif direction == 'right':
            player.orientation = 'E'
            # Check map collision
            if player.pos[0] < WIDTH_MAP - 1 and self.map[player.pos[1]][player.pos[0]+1] != 'm' and self.map[player.pos[1]][player.pos[0]+1] != '%' and self.map[player.pos[1]][player.pos[0]+1] != '$':
                # Check player collision
                for other_player in self.players:
                    if player != other_player:
                        if other_player.pos[0] == player.pos[0] + 1 and other_player.pos[1] == player.pos[1]:
                            return
                player.pos[0] += 1
        elif direction == 'left':
            player.orientation = 'W'
            # Check map collision
            if player.pos[0] > 0 and self.map[player.pos[1]][player.pos[0]-1] != 'm' and self.map[player.pos[1]][player.pos[0]-1] != '%' and self.map[player.pos[1]][player.pos[0]-1] != '$':
                # Check player collision
                for other_player in self.players:
                    if player != other_player:
                        if other_player.pos[0] == player.pos[0] - 1 and other_player.pos[1] == player.pos[1]:
                            return
                player.pos[0] -= 1

    def shoot(self, player):
        if player.ammunations > 0:
            rocket = Rocket(player.team, player.pos, player.orientation)
            player.ammunations -= 1
            self.rockets.append(rocket)
            self.callback_rocket(rocket, True)
            
    def callback_rocket(self, rocket, first_call):
        # Check for explosion
        t = None
        if not first_call:
            for player in self.players:
                if player.pos[0] == rocket.position[0] and player.pos[1] == rocket.position[1]:
                    rocket.explosion = True
                    player.decrease_life()
                    t = threading.Timer(FREQ_ROCKET, self.callback_rocket_has_exploded, args=[rocket])

        if rocket.orientation == 'N':
            if rocket.position[1] == 0 or self.map[rocket.position[1] - 1][rocket.position[0]] == 'm':
                rocket.explosing = True
                t = threading.Timer(FREQ_ROCKET, self.callback_rocket_has_exploded, args=[rocket])
        if rocket.orientation == 'E':
            if rocket.position[0] == WIDTH_MAP - 1 or self.map[rocket.position[1]][rocket.position[0] + 1] == 'm':
                rocket.explosing = True
                t = threading.Timer(FREQ_ROCKET, self.callback_rocket_has_exploded, args=[rocket])
        if rocket.orientation == 'S':
            if rocket.position[1] == HEIGHT_MAP - 1 or self.map[rocket.position[1] + 1][rocket.position[0]] == 'm':
                rocket.explosing = True
                t = threading.Timer(FREQ_ROCKET, self.callback_rocket_has_exploded, args=[rocket])
        if rocket.orientation == 'W':
            if rocket.position[0] == 0 or self.map[rocket.position[1]][rocket.position[0] - 1] == 'm':
                rocket.explosing = True
                t = threading.Timer(FREQ_ROCKET, self.callback_rocket_has_exploded, args=[rocket])

        if t == None:
            # Make rocket progress
            if rocket.orientation == 'N':
                rocket.position[1] -= 1
            elif rocket.orientation == 'E':
                rocket.position[0] += 1
            elif rocket.orientation == 'S':
                rocket.position[1] += 1
            elif rocket.orientation == 'W':
                rocket.position[0] -= 1
            t = threading.Timer(FREQ_ROCKET, self.callback_rocket, args=[rocket, False])
        t.start()

    def callback_rocket_has_exploded(self, rocket):
        self.rockets.remove(rocket)
                
    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.move(self.players[0], 'down')
            elif event.key == pygame.K_UP:
                self.move(self.players[0], 'up')
            elif event.key == pygame.K_RIGHT:
                self.move(self.players[0], 'right')
            elif event.key == pygame.K_LEFT:
                self.move(self.players[0], 'left')
            elif event.key == pygame.K_SPACE:
                self.shoot(self.players[0])

            if self.nb_human_player == 2:
                if event.key == pygame.K_s:
                    self.move(self.players[1], 'down')
                elif event.key == pygame.K_z:
                    self.move(self.players[1], 'up')
                elif event.key == pygame.K_d:
                    self.move(self.players[1], 'right')
                elif event.key == pygame.K_q:
                    self.move(self.players[1], 'left')
                elif event.key == pygame.K_LALT:
                    self.shoot(self.players[1])

        # TODO: check for winner

    def refresh_base(self):
        for player in self.players:
            if (player.team == Team.BLUE and player.pos[0] == 0 and player.pos[1] == HEIGHT_MAP - 1) or (player.team == Team.RED and player.pos[0] == WIDTH_MAP - 1 and player.pos[1] == 0):
                for timer in self.base_timers:
                    if timer[1] == player:
                        if timer[0] + DELAY_BASE < time.time():
                            player.increase_life()
                            player.increase_ammunations()
                            timer[0] = time.time()
                        return
                # No timer found, so add one
                self.base_timers.append([time.time(), player])
            else :
                # Remove old timers if they still exist
                for timer in self.base_timers:
                    if timer[1] == player:
                        self.base_timers.remove(timer)

    def refresh(self):
        self.refresh_base()