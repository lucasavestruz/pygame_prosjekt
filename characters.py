import pygame as pg
import random
from constants import *
from photos import *

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT
        self.speed = BULLET_SPEED

    # opptaterer skuddenes posijson
    def update(self):
        self.y -= self.speed

    # tegner skuddene
    def draw(self, screen):
        pg.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

class Player:
    def __init__(self):
        self.image = player_image
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.speed = PLAYER_SPEED
        self.bullets = []


    #håndterer bevegelse til spillern
    def handle_movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pg.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed


    #skyter skuddene
    def shoot(self):
        bullet_x = self.x + self.width // 2 - BULLET_WIDTH // 2
        bullet_y = self.y
        self.bullets.append(Bullet(bullet_x, bullet_y))


    #opptaterer posisjonen til skuddene
    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()
        self.bullets = [b for b in self.bullets if b.y > 0]


    #sjekker om skuddene kolliderer med fienden
    def check_collisions(self, enemies):
        enemies_hit = 0
        for bullet in self.bullets[:]:
            for enemy in enemies[:]:
                if enemy.check_collision(bullet):
                    self.bullets.remove(bullet)
                    enemies.remove(enemy)
                    enemies_hit += 1
        return enemies_hit
    

    #tegner spilleren og skuddene
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullets:
            bullet.draw(screen)

class Enemy:
    def __init__(self):
        self.image = enemy_image
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = -self.height
        self.speed = ENEMY_SPEED

    #opptaterer posisjonen til fienden
    def update(self):
        self.y += self.speed


    #tegner fienden
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

        
    #sjekker om fienden kolliderer med skuddene
    def check_collision(self, bullet):
        enemy_rect = pg.Rect(self.x, self.y, self.width, self.height)
        bullet_rect = pg.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
        return enemy_rect.colliderect(bullet_rect)

class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.last_spawn_time = pg.time.get_ticks() 

    #genererer fiender jevnlig
    def spawn_enemies(self):
        current_time = pg.time.get_ticks()
        if current_time - self.last_spawn_time > ENEMY_SPAWN_TIME:
            self.enemies.append(Enemy())
            self.last_spawn_time = current_time
    

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()
            if enemy.y > SCREEN_HEIGHT:
                return True
        return False
               
        
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)