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
game_over = False
game_over_time = 0


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.shoot()

    if not game_over:
    
        player.handle_movement()
        player.update_bullets()
        enemy_manager.spawn_enemies()
        enemy_manager.update_enemies()

    
        enemies_hit = player.check_collisions(enemy_manager.enemies)
        score += enemies_hit


        for enemy in enemy_manager.enemies:
            if enemy.y > SCREEN_HEIGHT:
                game_over = True
                game_over_time = pg.time.get_ticks()

    
        screen.fill(BLACK)

    
        player.draw(screen)
        enemy_manager.draw(screen)

    
        text.text_score(screen, f"Score: {score}", 10, 10, WHITE, BLACK)

    else:
  
        screen.fill(BLACK)
        text.text_game_over(screen, "Du tapte!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, (255, 0, 0), BLACK)
        text.text_game_over(screen, f"Score: {score}", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, WHITE, BLACK)

    
        if pg.time.get_ticks() - game_over_time > 5000:
        
            score = 0
            player = Player()
            enemy_manager = EnemyManager()
            game_over = False

    pg.display.update()

    clock.tick(60)

pg.quit()