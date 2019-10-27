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

class AI_Player(Player):
    def __init__(self, team):
        super().__init__(team)

    def play(self, game):
        if self.pos[0] > 0:
            left_cell = game.map[self.pos[1]][self.pos[0] - 1]
        else:
            left_cell = 'm'
        if self.pos[0] < 13 - 1:
            right_cell = game.map[self.pos[1]][self.pos[0] + 1]
        else:
            right_cell = 'm'
        if self.pos[1] > 0:
            top_cell = game.map[self.pos[1] - 1][self.pos[0]]
        else:
            top_cell = 'm'
        if self.pos[1] < 12 - 1:
            bottom_cell = game.map[self.pos[1] + 1][self.pos[0]]
        else:
            bottom_cell = 'm'

        #Considerer les barbeles comme des murs
        if left_cell == "%" or left_cell == "$":
            left_cell = "m"
        if right_cell == "%" or right_cell == "$":
            right_cell = "m"
        if top_cell == "%" or top_cell == "$":
            top_cell = "m"
        if bottom_cell == "%" or bottom_cell == "$":
            bottom_cell = "m"

        # Here we consider only one opponent
        for player in game.players:
            if player.team != self.team:
                foe = player
                break
        
        if foe.pos[0] > self.pos[0]:
            plus = "adroite"
        elif foe.pos[0] < self.pos[0]:
            plus = "agauche"
        elif foe.pos[0] == self.pos[0]:
            plus = "meme"
        if foe.pos[1] > self.pos[1]:
            plusV = "enbas"
        elif foe.pos[1] < self.pos[1]:
            plusV = "enhaut"
        elif foe.pos[1] == self.pos[1]:
            plusV = "meme"

        # Bouger
        if plus == "agauche" and plusV == "meme" and left_cell != "m" and self.pos[0] > 0:
            game.move(self, "left")
        elif plus == "adroite" and plusV == "meme" and right_cell != "m" and self.pos[0] < 13 - 1:
            game.move(self, "droite")
        elif plus == "meme" and plusV == "enhaut" and top_cell != "m" and self.pos[1] > 0:
            game.move(self, "haut")
        elif plus == "meme" and plusV == "enbas" and bottom_cell != "m" and self.pos[1] < 12 - 1:
            game.move(self, "down")
        elif plus == "agauche" and plusV == "enhaut":
            if top_cell == "m" and left_cell != "m" and self.pos[0] > 0:
                game.move(self, "left")
            elif top_cell != "m" and left_cell == "m" and self.pos[1] > 0:
                game.move(self, "up")
            elif top_cell == "m" and left_cell == "m" and self.pos[0] < 13 - 1:
                game.move(self, "right")
            elif top_cell != "m" and left_cell != "m" and self.pos[1] > 0:
                game.move(self, "up")
        elif plus == "adroite" and plusV == "enhaut":
            if top_cell == "m" and right_cell != "m" and self.pos[0] < 13 - 1:
                game.move(self, "droite")
            elif top_cell != "m" and right_cell == "m" and self.pos[1] > 0:
                game.move(self, "up")
            elif top_cell == "m" and right_cell == "m" and self.pos[0] > 0:
                game.move(self, "left")
            elif top_cell != "m" and right_cell != "m" and self.pos[1] > 0:
                game.move(self, "up")
        elif plus == "adroite" and plusV == "enbas":
            if bottom_cell == "m" and right_cell != "m" and self.pos[0] < 13 - 1:
                game.move(self, "right")
            elif bottom_cell != "m" and right_cell == "m" and self.pos[1] < 12 - 1:
                game.move(self, "down")
            elif bottom_cell == "m" and right_cell == "m" and self.pos[0] > 0:
                game.move(self, "left")
            elif bottom_cell != "m" and right_cell != "m" and self.pos[1] < 12 - 1:
                game.move(self, "down")
        elif plus == "agauche" and plusV == "enbas":
            if bottom_cell == "m" and left_cell != "m" and self.pos[0] > 0:
                game.move(self, "left")
            elif bottom_cell != "m" and left_cell == "m" and self.pos[1] < 12 - 1:
                game.move(self, "down")
            elif bottom_cell == "m" and left_cell == "m" and self.pos[0] < 13 - 1:
                game.move(self, "right")
            elif bottom_cell != "m" and left_cell != "m" and self.pos[1] < 12 - 1:
                game.move(self, "down")

        #Contourner les murs
        elif plus == "agauche" and plusV == "meme" and left_cell == "m" and bottom_cell != "m" and self.pos[1] < 550:
            game.move(self, "down")
        elif plus == "agauche" and plusV == "meme" and left_cell == "m" and bottom_cell == "m" and self.pos[1] > 0:
            game.move(self, "up")
        elif plus == "adroite" and plusV == "meme" and right_cell == "m" and bottom_cell != "m" and self.pos[1] < 550:
            game.move(self, "down")
        elif plus == "adroite" and plusV == "meme" and right_cell == "m" and bottom_cell == "m" and self.pos[1] > 0:
            game.move(self, "up")
        elif plus == "meme" and plusV == "enhaut" and top_cell == "m" and left_cell != "m" and self.pos[0] > 0:
            game.move(self, "left")
        elif plus == "meme" and plusV == "enhaut" and top_cell == "m" and left_cell == "m" and self.pos[0] < 13 - 1:
            game.move(self, "right")
        elif plus == "meme" and plusV == "enbas" and bottom_cell == "m" and left_cell != "m" and self.pos[0] > 0:
            game.move(self, "left")
        elif plus == "meme" and plusV == "enbas" and bottom_cell == "m" and left_cell == "m" and self.pos[0] > 13 - 1:
            game.move(self, "right")

        #Tirer !
        if self.orientation == "W" and plus == "agauche" and plusV == "meme" and left_cell != "m" and self.pos[0] > 0:
            game.shoot(self)
        elif self.orientation == "E" and plus == "adroite" and plusV == "meme" and right_cell != "m"  and self.pos[0] < 13 - 1:
            game.shoot(self)
        elif self.orientation == "N" and plus == "meme" and plusV == "enhaut" and top_cell != "m" and self.pos[1] > 0:
            game.shoot(self)
        elif self.orientation == "S" and plus == "meme" and plusV == "enbas" and bottom_cell != "m" and self.pos[1] < 12 - 1:
            game.shoot(self)