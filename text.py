import pygame as pg

font = pg.font.SysFont("Arial", 32)

def text(screen, x, y, tekst, farge, bakgrunnsfarge):

    tekst_surface = font.render(tekst, True, farge)
    back_surface = pg.Surface(tekst_surface.get_size())
    back_surface.fill(bakgrunnsfarge)
    back_surface.blit(tekst_surface, (0, 0))
    screen.blit(back_surface, (x, y))
    





