import pygame as pg
from constants import *

pg.init()
screen = pg.display.set_mode((SCREEN_SIZE))
clock = pg.time.Clock()

from photos import *
from characters import Player, EnemyManager
import text

player = Player()
enemy_manager = EnemyManager()


score = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()

    # objektene opptatereres
    player.handle_movement()
    player.update_bullets()
    enemy_manager.spawn_enemies()
    enemy_manager.update_enemies()

    # sjekker kollisjon og legger til score
    enemies_hit = player.check_collisions(enemy_manager.enemies)
    score += enemies_hit 

    #bakgrunnsfarge
    screen.fill(BLACK)

    #tegner objektene
    player.draw(screen)
    enemy_manager.draw(screen)


    #viser poengsummen
    text.text(screen, f"{score}", 10, 10, WHITE, BLACK)

    pg.display.update()

    clock.tick(60)

pg.quit()