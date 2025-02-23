import pygame as pg
from constants import *

enemy_image = pg.image.load("assets/enemy.png").convert_alpha()
player_image = pg.image.load("assets/player.png").convert_alpha()

enemy_image = pg.transform.scale(enemy_image, (ENEMY_WIDTH, ENEMY_HEIGHT))
player_image = pg.transform.scale(player_image, (PLAYER_WIDTH, PLAYER_HEIGHT))