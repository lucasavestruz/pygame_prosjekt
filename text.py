import pygame as pg

font = pg.font.SysFont("Arial", 32)

def text(screen, text, x, y, color, backgroundColor):
    tekst_surface = font.render(text, True, color)
    back_surface = pg.Surface(tekst_surface.get_size())
    back_surface.fill(backgroundColor)
    back_surface.blit(tekst_surface, (0, 0))
    screen.blit(back_surface, (x, y))


 