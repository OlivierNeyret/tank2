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

from game import Game
import enum

NB_MAP = 3

class GM_choice(enum.Enum):
    VICTORY_BLUE = 1
    VICTORY_RED = 2
    FINAL_VICTORY_BLUE = 3
    FINAL_VICTORY_RED = 4

class Games_Manager:
    def __init__(self, nb_human_player, map_number = 0, difficulty = Difficulty.NONE):
        self.difficulty = difficulty
        self.nb_human_player = nb_human_player
        # If map_number == 0 then play on the three maps
        self.map_number = map_number
        if map_number == 0:
            self.current_map = 1
        else:
            self.current_map = map_number
        self.nb_victory_blue = 0
        self.nb_victory_red = 0

    def launch_game(self):
        if self.map_number == 0:
            return Game(self.nb_human_player, self.current_map)
        else:
            return Game(self.nb_human_player, self.map_number)

    def game_over(self, winner):
        if self.map_number == 0:
            if winner == "blue":
                self.nb_victory_blue += 1
            elif winner == "red":
                self.nb_victory_red += 1

            if self.current_map < NB_MAP:
                self.current_map += 1
                if winner == "blue":
                    return GM_choice.VICTORY_BLUE
                elif winner == "red":
                    return GM_choice.VICTORY_RED
            else:
                if winner == "blue":
                    return GM_choice.FINAL_VICTORY_BLUE
                elif winner == "red":
                    return GM_choice.FINAL_VICTORY_RED
        else:
            if winner == "blue":
                return GM_choice.FINAL_VICTORY_BLUE
            elif winner == "red":
                return GM_choice.FINAL_VICTORY_RED