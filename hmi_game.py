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

import pygame

class HMI_game:
    def __init__(self, window):
        self.window = window
        self.menu_background = pygame.image.load("images/info_bar/menu_background.png").convert()
        # Maps sprites
        self.wall = pygame.image.load("images/maps/wall.png").convert()
        self.road_h = pygame.image.load("images/maps/road_h.png").convert()
        self.road_v = pygame.image.load("images/maps/road_v.png").convert()
        self.road_turn_sw = pygame.image.load("images/maps/road_turn_sw.png").convert()
        self.road_turn_nw = pygame.image.load("images/maps/road_turn_nw.png").convert()
        self.road_turn_ne = pygame.image.load("images/maps/road_turn_ne.png").convert()
        self.road_turn_se= pygame.image.load("images/maps/road_turn_se.png").convert()
        self.grass = pygame.image.load("images/maps/grass.png").convert()
        self.intersection_vw = pygame.image.load("images/maps/intersection_vw.png").convert()
        self.intersection_hs = pygame.image.load("images/maps/intersection_hs.png").convert()
        self.intersection_ve = pygame.image.load("images/maps/intersection_ve.png").convert()
        self.intersection_hn = pygame.image.load("images/maps/intersection_hn.png").convert()
        self.crossroads_v = pygame.image.load("images/maps/crossroads_v.png").convert()
        self.crossroads_h = pygame.image.load("images/maps/carrefour_h.png").convert()
        self.barbed_wire_v = pygame.image.load("images/maps/barbed_wire_v.png").convert()
        self.barbed_wire_h = pygame.image.load("images/maps/barbed_wire_h.png").convert()
        self.base_blue = pygame.image.load("images/maps/base_blue.png").convert()
        self.base_red = pygame.image.load("images/maps/base_red.png").convert()
        # Digits
        self.zero = pygame.image.load("images/characters/zero.png").convert_alpha()
        self.one = pygame.image.load("images/characters/one.png").convert_alpha()
        self.two = pygame.image.load("images/characters/two.png").convert_alpha()
        self.three = pygame.image.load("images/characters/three.png").convert_alpha()
        self.four = pygame.image.load("images/characters/four.png").convert_alpha()
        self.five = pygame.image.load("images/characters/five.png").convert_alpha()
        self.six = pygame.image.load("images/characters/six.png").convert_alpha()
        self.seven = pygame.image.load("images/characters/seven.png").convert_alpha()
        self.eight = pygame.image.load("images/characters/eight.png").convert_alpha()
        self.nine = pygame.image.load("images/characters/nine.png").convert_alpha()
        self.level = pygame.image.load("images/characters/level.png").convert_alpha()
        # Life bar
        self.life_bar_100 = pygame.image.load("images/info_bar/life_100.jpg").convert_alpha()
        self.life_bar_80 = pygame.image.load("images/info_bar/life_80.jpg").convert_alpha()
        self.life_bar_60 = pygame.image.load("images/info_bar/life_60.jpg").convert_alpha()
        self.life_bar_40 = pygame.image.load("images/info_bar/life_40.jpg").convert_alpha()
        self.life_bar_20 = pygame.image.load("images/info_bar/life_20.jpg").convert_alpha()
        self.life_bar_0 = pygame.image.load("images/info_bar/life_0.jpg").convert_alpha()
        # Tank
        self.tank_blue_100 = pygame.image.load("images/info_bar/tank_blue_100.png").convert_alpha()
        self.tank_blue_80 = pygame.image.load("images/info_bar/tank_blue_80.png").convert_alpha()
        self.tank_blue_60 = pygame.image.load("images/info_bar/tank_blue_60.png").convert_alpha()
        self.tank_blue_40 = pygame.image.load("images/info_bar/tank_blue_40.png").convert_alpha()
        self.tank_blue_20 = pygame.image.load("images/info_bar/tank_blue_20.png").convert_alpha()
        self.tank_red_100 = pygame.image.load("images/info_bar/tank_red_100.png").convert_alpha()
        self.tank_red_80 = pygame.image.load("images/info_bar/tank_red_80.png").convert_alpha()
        self.tank_red_60 = pygame.image.load("images/info_bar/tank_red_60.png").convert_alpha()
        self.tank_red_40 = pygame.image.load("images/info_bar/tank_red_40.png").convert_alpha()
        self.tank_red_20 = pygame.image.load("images/info_bar/tank_red_20.png").convert_alpha()
        # Misc
        self.bullet = pygame.image.load("images/info_bar/bullet.png").convert_alpha()
        self.rocket_blue = pygame.image.load("images/rocket_blue.png").convert_alpha()
        self.rocket_red = pygame.image.load("images/rocket_red.png").convert_alpha()
        self.explosion = pygame.image.load("images/explosion.png").convert_alpha()
        # Victory screens
        self.blue_victory = pygame.image.load("images/victory_screens/blue_victory.png").convert_alpha()
        self.red_victory = pygame.image.load("images/victory_screens/red_victory.png").convert_alpha()
        self.final_blue_victory = pygame.image.load("images/victory_screens/final_blue_victory.png").convert_alpha()
        self.final_red_victory = pygame.image.load("images/victory_screens/final_red_victory.png").convert_alpha()

        # Sounds
        self.explosion_sound = pygame.mixer.Sound("audio/explosion.wav")
        self.missile_sound = pygame.mixer.Sound("audio/rocket.ogg")
        self.red_victory_sound = pygame.mixer.Sound("audio/red_victory.wav")
        self.blue_victory_sound = pygame.mixer.Sound("audio/blue_victory.wav")

    def display(self):
        pass

    def event(self, event):
        pass