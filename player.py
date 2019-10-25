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

import enum

class Team(enum.Enum):
    BLUE = 1
    RED = 2

class Player:
    def __init__(self, team):
        self.life = 100
        self.ammunations = 8
        self.team = team
        if team == Team.BLUE:
            self.pos = [0, 11]
            self.orientation = 'E'
        elif team == Team.RED:
            self.pos = [12, 0]
            self.orientation = 'W'