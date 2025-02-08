import os
import traceback
from ast import literal_eval
from shutil import move as shutil_move

import pygame
import ujson

from scripts.event_class import Single_Event
from scripts.game_structure.screen_settings import toggle_fullscreen
from scripts.housekeeping.datadir import get_save_dir, get_temp_dir

pygame.init()

from scripts.game_structure import game

if not os.path.exists(get_save_dir() + "/settings.txt"):
    os.makedirs(get_save_dir(), exist_ok=True)
    with open(get_save_dir() + "/settings.txt", "w", encoding="utf-8") as write_file:
        write_file.write("")
game.load_settings()

pygame.display.set_caption("Clan Generator")

toggle_fullscreen(
    fullscreen=game.settings["fullscreen"],
    show_confirm_dialog=False,
    ingame_switch=False,
)
