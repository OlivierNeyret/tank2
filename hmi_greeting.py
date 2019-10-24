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
import enum

SOUND_X_POS = 530
SOUND_Y_POS = 390

class HMI_greeting_choice(enum.Enum):
    NOTHING = 0
    LAUNCH_ONE_PLAYER_EASY = 1
    LAUNCH_ONE_PLAYER_MEDIUM = 2
    LAUNCH_ONE_PLAYER_HARD = 3
    LAUNCH_TWO_PLAYER = 4
    SWITCH_SOUND = 5

class HMI_greeting_screen(enum.Enum):
    GREETING = 0
    ONE_PLAYER_RULES = 1
    TWO_PLAYER_RULES = 2
    DIFFICULTY = 3

class HMI_greeting:
    def __init__(self, window):
        self.window = window
        self.greeting_background = pygame.image.load("images/greeting_background.png").convert()
        self.one_player_background = pygame.image.load("images/one_player_background.png").convert()
        self.two_player_background = pygame.image.load("images/two_player_background.png").convert()
        self.difficulty_background = pygame.image.load("images/difficulty_background.png").convert()
        self.sound_on = pygame.image.load("images/sound_on.png").convert_alpha()
        self.sound_off = pygame.image.load("images/sound_off.png").convert_alpha()
        self.current_screen = HMI_greeting_screen.GREETING
        self.choosed_difficulty = 0

    def display(self, play_sound):
        if self.current_screen == HMI_greeting_screen.GREETING:
            self.window.blit(self.greeting_background, (0, 0))
        elif self.current_screen == HMI_greeting_screen.ONE_PLAYER_RULES:
            self.window.blit(self.one_player_background, (0, 0))
        elif self.current_screen == HMI_greeting_screen.TWO_PLAYER_RULES:
            self.window.blit(self.two_player_background, (0, 0))
        elif self.current_screen == HMI_greeting_screen.DIFFICULTY:
            self.window.blit(self.difficulty_background, (0, 0))

        if play_sound:
            self.window.blit(self.sound_on, (SOUND_X_POS, SOUND_Y_POS))
        else:
            self.window.blit(self.sound_off, (SOUND_X_POS, SOUND_Y_POS))
        pygame.display.flip()

    def event(self, event):
        if self.current_screen == HMI_greeting_screen.GREETING:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 48<event.pos[0]<274 and 156<event.pos[1]<202:
                self.current_screen = HMI_greeting_screen.DIFFICULTY
                return HMI_greeting_choice.NOTHING
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 48<event.pos[0]<274 and    288<event.pos[1]<330:
                self.current_screen = HMI_greeting_screen.TWO_PLAYER_RULES
                return HMI_greeting_choice.NOTHING
            elif event.type  == pygame.MOUSEBUTTONDOWN and event.button == 1 and 530<event.pos[0]<730 and 390<event.pos[1]<440:
                return HMI_greeting_choice.SWITCH_SOUND
        elif self.current_screen == HMI_greeting_screen.ONE_PLAYER_RULES:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.current_screen = HMI_greeting_screen.GREETING
                if self.choosed_difficulty == 1:
                    return HMI_greeting_choice.LAUNCH_ONE_PLAYER_EASY
                elif self.choosed_difficulty == 2:
                    return HMI_greeting_choice.LAUNCH_ONE_PLAYER_MEDIUM
                elif self.choosed_difficulty == 3:
                    return HMI_greeting_choice.LAUNCH_ONE_PLAYER_HARD
        elif self.current_screen == HMI_greeting_screen.TWO_PLAYER_RULES:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.current_screen = HMI_greeting_screen.GREETING
                return HMI_greeting_choice.LAUNCH_TWO_PLAYER
        elif self.current_screen == HMI_greeting_screen.DIFFICULTY:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 56<event.pos[0]<210 and 220<event.pos[1]<254:
                self.current_screen = HMI_greeting_screen.ONE_PLAYER_RULES
                self.choosed_difficulty = 1
                return HMI_greeting_choice.NOTHING
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 56<event.pos[0]<210 and 287<event.pos[1]<322:
                self.current_screen = HMI_greeting_screen.ONE_PLAYER_RULES
                self.choosed_difficulty = 2
                return HMI_greeting_choice.NOTHING
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and 56<event.pos[0]<210 and 347<event.pos[1]<381:
                self.current_screen = HMI_greeting_screen.ONE_PLAYER_RULES
                self.choosed_difficulty = 3
                return HMI_greeting_choice.NOTHING
        return HMI_greeting_choice.NOTHING
            