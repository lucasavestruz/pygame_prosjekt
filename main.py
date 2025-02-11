import pygame as pg
from constants import *
import tkinter as tk

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((SIZE))

from characters import Player
from characters import Enemy
import text
from photos import *




circle = Player(100, 100, 25, (255, 0, 0))

ball1 = Enemy(farge=BLUE, radius=40, x=50, y=100, dx=5, dy=3)
ball2 = Enemy(farge=GREEN, radius=20, x=200, y=200, dx=-5, dy=3)

def start_game():
    circle.move()
    circle.kollisjon_med_vegg()
    pg.draw.circle(screen, circle.color, (circle.x, circle.y), circle.radius)
    ball1.tegn(screen)
    ball2.tegn(screen)
    ball1.oppdater()
    ball2.oppdater()
    ball1.kollisjon(ball2)
    ball1.kollisjon_med_player(circle)
    ball2.kollisjon_med_player(circle)





running = True
game_started = False
while running:
    screen.fill((255, 255, 255))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                game_started = True
    

    if game_started:
        start_game()
    else:
        text.text(screen, 350, 350, "Trykk Enter for å starte", BLACK, WHITE)
    



    clock.tick(FPS)
    screen.blit(bg_image, (0, 0))
    pg.display.update()


pg.quit()
