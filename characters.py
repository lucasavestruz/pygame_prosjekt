import pygame as pg
from constants import *
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_RETURN)
import text



class Player:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    
    def move(self):
        keys_pressed = pg.key.get_pressed()

        if keys_pressed[pg.K_UP]:
            self.y -= PLAYER_SPEED
        elif keys_pressed[pg.K_DOWN]:
            self.y += PLAYER_SPEED
        elif keys_pressed[pg.K_LEFT]:
            self.x -= PLAYER_SPEED
        elif keys_pressed[pg.K_RIGHT]:
            self.x += PLAYER_SPEED



    def kollisjon_med_vegg(self):
        if self.x < self.radius:
            self.x = self.radius
        elif self.x > WIDTH - self.radius:
            self.x = WIDTH - self.radius
        elif self.y < self.radius:
            self.y = self.radius
        elif self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius


class Enemy:

    def __init__(self, farge, radius, x, y, dx, dy):
        self.farge = farge
        self.radius = radius
        self.x = x
        self.y = y
        self.dx = dx 
        self.dy = dy

    def tegn(self, screen):
        pg.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def oppdater(self):
        self.x += self.dx 
        self.y += self.dy
   
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.dx = -self.dx
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.dy = -self.dy

    def kollisjon(self, ball):
        x_avst_kvadrat = (self.x - ball.x)**2
        y_avst_kvadrat = (self.y - ball.y)**2
        avst_mellom_ballene = (x_avst_kvadrat + y_avst_kvadrat)**0.5
        if (avst_mellom_ballene < self.radius + ball.radius):
      
            self.dx = -self.dx
            self.dy = -self.dy
            ball.dx = -ball.dx
            ball.dy = -ball.dy
    
    def kollisjon_med_player(self, player):
        x_avst_kvadrat = (self.x - player.x)**2
        y_avst_kvadrat = (self.y - player.y)**2
        avst_mellom_ballene = (x_avst_kvadrat + y_avst_kvadrat)**0.5
        if (avst_mellom_ballene < self.radius + player.radius):
            pass

         


            

           
           

    


        
 
     
