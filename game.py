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
import sys
import enum

class Difficulty(enum.Enum):
    NONE = 0
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Game:
    def __init__(self, nb_human_player, nb_ai_player, level):
        self.nb_human_player = nb_human_player
        self.players = []
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
                
    def event(self, event):
        pass