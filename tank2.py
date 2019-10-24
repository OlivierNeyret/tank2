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
from hmi_greeting import HMI_greeting, HMI_greeting_choice

WIDTH = 800
HEIGHT = 600

if __name__ == "__main__":
    continue_loop = True
    play_sound = False
    is_playing = False

    pygame.init()
    window = pygame.display.set_mode([WIDTH, HEIGHT])
    hmi_greeting = HMI_greeting(window)

    hmi_greeting.display(play_sound)

    while continue_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continue_loop = False
            if not is_playing:
                choice = hmi_greeting.event(event)
                if choice == HMI_greeting_choice.SWITCH_SOUND:
                    play_sound = not play_sound
                    hmi_greeting.display(play_sound)
                elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_EASY:
                    continue_loop = False
                elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_MEDIUM:
                    continue_loop = False
                elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_HARD:
                    continue_loop = False
                elif choice == HMI_greeting_choice.LAUNCH_TWO_PLAYER:
                    continue_loop = False
                elif choice == HMI_greeting_choice.NOTHING:
                    hmi_greeting.display(play_sound)
                
    pygame.quit()