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

from player import Team

class Rocket():
    def __init__(self, team, position, orientation):
        self.team = team
        self.position = []
        # Avoid non-copy problem
        self.position.append(position[0])
        self.position.append(position[1])
        self.orientation = orientation
        self.explosing = False