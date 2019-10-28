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
from hmi_greeting import HMI_greeting, HMI_greeting_choice
from hmi_game import HMI_game
from games_manager import Games_Manager, GM_choice
from game import Game, Difficulty

WIDTH_ONE_PLAYER = 800
WIDTH_TWO_PLAYER = 950
HEIGHT = 600

class Screen(enum.Enum):
    GREETING = 0
    PLAYING = 1
    VICTORY = 2
    FINAL_VICTORY = 3

if __name__ == "__main__":
    continue_loop = True
    play_sound = False
    current_screen = Screen.GREETING

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
            break
        if current_screen == Screen.GREETING:
            choice = hmi_greeting.event(event)
            if choice == HMI_greeting_choice.SWITCH_SOUND:
                play_sound = not play_sound
                hmi_greeting.display(play_sound)
            elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_EASY:
                games_manager = Games_Manager(1, map_number=0, difficulty=Difficulty.EASY)
                current_game = games_manager.launch_game()
                nb_human_player = 1
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                pygame.time.set_timer(pygame.USEREVENT, 20)
                pygame.time.set_timer(pygame.USEREVENT+1, Difficulty.EASY.value)
                current_screen = Screen.PLAYING
            elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_MEDIUM:
                games_manager = Games_Manager(1, map_number=0, difficulty=Difficulty.MEDIUM)
                current_game = games_manager.launch_game()
                nb_human_player = 1
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                pygame.time.set_timer(pygame.USEREVENT, 20)
                pygame.time.set_timer(pygame.USEREVENT+1, Difficulty.MEDIUM.value)
                current_screen = Screen.PLAYING
            elif choice == HMI_greeting_choice.LAUNCH_ONE_PLAYER_HARD:
                games_manager = Games_Manager(1, map_number=0, difficulty=Difficulty.HARD)
                current_game = games_manager.launch_game()
                nb_human_player = 1
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                pygame.time.set_timer(pygame.USEREVENT, 20)
                pygame.time.set_timer(pygame.USEREVENT+1, Difficulty.HARD.value)
                current_screen = Screen.PLAYING
            elif choice == HMI_greeting_choice.LAUNCH_TWO_PLAYER:
                games_manager = Games_Manager(2, map_number=0)
                current_game = games_manager.launch_game()
                window = pygame.display.set_mode([WIDTH_TWO_PLAYER, HEIGHT])
                nb_human_player = 2
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
                pygame.time.set_timer(pygame.USEREVENT, 20)
                current_screen = Screen.PLAYING
            elif choice == HMI_greeting_choice.NOTHING:
                hmi_greeting.display(play_sound)

        elif current_screen == Screen.PLAYING:
            if event.type == pygame.USEREVENT:
                winner = current_game.refresh()
                hmi_game.display(current_game, play_sound, nb_human_player == 2)
            elif event.type == pygame.USEREVENT + 1:
                current_game.play_ai()
            else:
                winner = current_game.event(event)
            if winner != None:
                gm_choice = games_manager.game_over(winner)
                hmi_game.display_winner(gm_choice, games_manager.nb_victory_blue, games_manager.nb_victory_red)
                if gm_choice == GM_choice.VICTORY_BLUE or gm_choice == GM_choice.VICTORY_RED:
                    current_screen = Screen.VICTORY
                else:
                    current_screen = Screen.FINAL_VICTORY

        elif current_screen == Screen.VICTORY:
            if event.type == pygame.MOUSEBUTTONDOWN:
                current_game = games_manager.launch_game()
                current_screen = Screen.PLAYING

        elif current_screen == Screen.FINAL_VICTORY:
            if event.type == pygame.MOUSEBUTTONDOWN:      
                current_game = None
                nb_human_player = 0
                pygame.time.set_timer(pygame.USEREVENT, 0)
                pygame.time.set_timer(pygame.USEREVENT+1, 0)
                current_screen = Screen.GREETING
                window = pygame.display.set_mode([WIDTH_ONE_PLAYER, HEIGHT])
                pygame.display.set_caption("Tank2")
                hmi_greeting.display(play_sound)

    pygame.quit()