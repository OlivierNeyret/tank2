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

WIDTH_SIDE_MENU = 150
WIDTH_SPRITE = 50
HEIGHT_SPRITE = 50

X_AMMUNATIONS_BLUE = 50
Y_AMMUNATIONS_BLUE = 235
X_AMMUNATIONS_RED = 850
Y_AMMUNATIONS_RED = 235

X_LIFE_BLUE = 40
Y_LIFE_BLUE = 550
X_LIFE_RED = 840
Y_LIFE_RED = 550

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
        self.crossroads_h = pygame.image.load("images/maps/crossroads_h.png").convert()
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

    def display_digits(self, number, x, y):
        if number >= 0:
            list_digit = [int(c) for c in str(number)]
            list_img = [self.zero, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine]
            i = 0
            for digit in list_digit:
                self.window.blit(list_img[list_digit[i]], (x, y))
                i += 1
                x += 25

    def display_ammunations(self, blue, nb_ammo):
        x = 0
        y = 0
        if blue:
            x = X_AMMUNATIONS_BLUE
            y = Y_AMMUNATIONS_BLUE
        else:
            x = X_AMMUNATIONS_RED
            y = Y_AMMUNATIONS_RED

        self.display_digits(nb_ammo, x, y)
        for i in range(nb_ammo):
            self.window.blit(self.bullet, ((x - 25) + (8 * i), y + 30))

    def display_life(self, blue, life):
        x = 0
        y = 0
        if blue:
            x = X_LIFE_BLUE
            y = Y_LIFE_BLUE
        else:
            x = X_LIFE_RED
            y = Y_LIFE_RED

        if life == 100:
            self.window.blit(self.life_bar_100, (x, y))
            if blue:
                self.window.blit(self.tank_blue_100, (x + 16, y - 50))
            else:
                self.window.blit(self.tank_red_100, (x + 16, y - 50))
        elif life == 80:
            self.window.blit(self.life_bar_80, (x, y))
            if blue:
                self.window.blit(self.tank_blue_80, (x + 16, y - 50))
            else:
                self.window.blit(self.tank_red_80, (x + 16, y - 50))
        elif life == 60:
            self.window.blit(self.life_bar_60, (x, y))
            if blue:
                self.window.blit(self.tank_blue_60, (x + 16, y - 50))
            else:
                self.window.blit(self.tank_red_60, (x + 16, y - 50))
        elif life == 40:
            self.window.blit(self.life_bar_40, (x, y))
            if blue:
                self.window.blit(self.tank_blue_40, (x + 16, y - 50))
            else:
                self.window.blit(self.tank_red_40, (x + 16, y - 50))
        elif life == 20:
            self.window.blit(self.life_bar_20, (x, y))
            if blue:
                self.window.blit(self.tank_blue_20, (x + 16, y - 50))
            else:
                self.window.blit(self.tank_red_20, (x + 16, y - 50))

    def display(self, game, play_sound, two_menu):
        # Display menu(s)
        self.window.blit(self.menu_background, (0, 0))
        ## Level
        # TODO!
        ## Ammunations
        self.display_ammunations(True, game.players[0].ammunations)
        ## Life
        self.display_life(True, game.players[0].life)

        if two_menu:
            self.window.blit(self.menu_background, (800, 0))
            self.display_ammunations(False, game.players[1].ammunations)
            self.display_life(False, game.players[1].life)

        # Display map
        idx_line = 0
        for line in game.map:
            idx_col = 0
            for sprite in line:
                x = (idx_col * WIDTH_SPRITE) + WIDTH_SIDE_MENU
                y = idx_line * HEIGHT_SPRITE
                if sprite == "m":
                    self.window.blit(self.wall, (x,y))
                elif sprite == "h":
                    self.window.blit(self.road_h, (x,y))
                elif sprite == "v":
                    self.window.blit(self.road_v, (x,y))
                elif sprite == "0":
                    self.window.blit(self.road_turn_sw, (x,y))
                elif sprite == "1":
                    self.window.blit(self.road_turn_nw, (x,y))
                elif sprite == "2":
                    self.window.blit(self.road_turn_ne, (x,y))
                elif sprite == "3":
                    self.window.blit(self.road_turn_se, (x,y))
                elif sprite == "w":
                    self.window.blit(self.grass, (x,y))
                elif sprite == "b":
                    self.window.blit(self.base_blue, (x,y))
                elif sprite == "c":
                    self.window.blit(self.base_red, (x,y))
                elif sprite == "%":
                    self.window.blit(self.barbed_wire_v, (x,y))
                elif sprite == "$":
                    self.window.blit(self.barbed_wire_h, (x,y))
                elif sprite == "4":
                    self.window.blit(self.intersection_vw, (x,y))
                elif sprite == "5":
                    self.window.blit(self.intersection_hs, (x,y))
                elif sprite == "6":
                    self.window.blit(self.intersection_ve, (x,y))
                elif sprite == "7":
                    self.window.blit(self.intersection_hn, (x,y))
                elif sprite == "8":
                    self.window.blit(self.crossroads_v, (x,y))
                elif sprite == "9":
                    self.window.blit(self.crossroads_h, (x,y))
                idx_col += 1
            idx_line += 1
        pygame.display.flip()

    def event(self, event):
        pass