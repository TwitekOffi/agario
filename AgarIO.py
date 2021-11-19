import random
import pygame
from pygame.math import Vector2
import core
from Creep import Creep
from Ennemi import Ennemi
from Joueur import Joueur


def setup():
    print("Setup START---------")
    core.fps = 60
    core.WINDOW_SIZE = [1080, 720]

    core.memory("TabDeCreep", [])
    core.memory("TabDeEnnemi", [])
    core.memory("Joueur", Joueur())

    for i in range(200):
        core.memory("TabDeCreep").append(Creep())

    for i in range(5):
        core.memory("TabDeEnnemi").append(Ennemi())
    print("Setup END-----------")


def run():
    core.cleanScreen()

    # AFFICHAGE
    for i in core.memory("TabDeCreep"):
        i.draw(core.screen)

    for i in core.memory("TabDeEnnemi"):
        i.draw(core.screen)
    core.memory("Joueur").draw(core.screen)
    # AFFICHAGE

    # DEPLACER
    core.memory("Joueur").deplacer(720,1080, core.getMouseLeftClick())
    for i in core.memory("TabDeEnnemi"):
        i.deplacer(720,1080)

    # DEPLACER

    # COLISION
    for i in core.memory("TabDeCreep"):
        if i.position.distance_to(core.memory("Joueur").position) < (core.memory("Joueur").rayon + i.rayon):
            core.memory("Joueur").grossir()
            i.mourir()
        for e in core.memory("TabDeEnnemi"):
            if i.position.distance_to(e.position) < (e.rayon + i.rayon):
                e.grossir()
                i.mourir()

    for e in core.memory("TabDeEnnemi"):
        if e.position.distance_to(core.memory("Joueur").position) < (core.memory("Joueur").rayon + e.rayon):
            if core.memory("Joueur").rayon < e.rayon:
                core.memory("Joueur").mourir()
            else:
                e.mourir()

    # COLISION


core.main(setup, run)
