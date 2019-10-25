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
from hmi_game import HMI_game
from games_manager import Games_Manager, GM_choice
from game import Game, Difficulty

WIDTH_ONE_PLAYER = 800
WIDTH_TWO_PLAYER = 950
HEIGHT = 600

if __name__ == "__main__":
    continue_loop = True
    play_sound = False
    is_playing = False

    pygame.init()

    pygame.mixer.quit()

    window = pygame.display.set_mode([WIDTH_ONE_PLAYER, HEIGHT])
    pygame.display.set_caption("Tank2")
    hmi_greeting = HMI_greeting(window)
    hmi_game = HMI_game(window)
    games_manager = None
    current_game = None
    nb_human_player = 0

    hmi_greeting.display(play_sound)

    while continue_loop:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            continue_loop = False
        if not is_playing:
            choice = hmi_greeting.event(event)
            if choice == HMI_greeting_choice.SWITCH_SOUND:
                play_sound = not play_sound
                hmi_greeting.display(play_sound)
            elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_EASY:
                games_manager = Games_Manager(1, map_number=0, difficulty=Difficulty.EASY)
                current_game = games_manager.launch_game()
                nb_human_player = 1
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                is_playing = True
            elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_MEDIUM:
                games_manager = Games_Manager(1, map_number=0, difficulty=Difficulty.MEDIUM)
                current_game = games_manager.launch_game()
                nb_human_player = 1
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                is_playing = True
            elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_HARD:
                games_manager = Games_Manager(1, map_number=0, difficulty=Difficulty.HARD)
                current_game = games_manager.launch_game()
                nb_human_player = 1
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                is_playing = True
            elif choice == HMI_greeting_choice.LAUNCH_TWO_PLAYER:
                games_manager = Games_Manager(2, map_number=0)
                current_game = games_manager.launch_game()
                window = pygame.display.set_mode([WIDTH_TWO_PLAYER, HEIGHT])
                nb_human_player = 2
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                is_playing = True
            elif choice == HMI_greeting_choice.NOTHING:
                hmi_greeting.display(play_sound)
        else:
            current_game.event(event)
            hmi_game.display(current_game, play_sound, nb_human_player == 2)
                
    pygame.quit()