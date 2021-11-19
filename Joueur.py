import random
import pygame
from pygame.math import Vector2
import core


class Joueur:
    def __init__(self):
        self.vitesseMax = 8
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))
        self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))
        self.rayon = 5
        self.nom = "Test"
        self.direction = Vector2(0, 0)

        self.Fx = 0
        self.Ux = Vector2(0, 0)
        self.l = 0
        self.l0 = 10
        self.L = 0

    def mourir(self):
        self.rayon = 5

    def grossir(self):
        if self.rayon < 200:
            self.rayon = self.rayon + 1
        self.vitesseMax = self.vitesseMax * 0.95

    def deplacer(self, h, l, clique):
        if core.getKeyPressList(pygame.K_SPACE):
            self.direction = Vector2(0, 0)

            # if core.getKeyPressList(pygame.K_z):
            #    self.direction = Vector2(self.direction.x, -1)
            # if core.getKeyPressList(pygame.K_s):
            #     self.direction = Vector2(self.direction.x, 1)
            # if core.getKeyPressList(pygame.K_q):
            #    self.direction = Vector2(-1, self.direction.y)
            # if core.getKeyPressList(pygame.K_d):
            #     self.direction = Vector2(1, self.direction.y)
            # if self.position.y < 0 or self.position.y > core.WINDOW_SIZE[1]:
            #     self.direction = Vector2(self.direction.x, self.direction.y * -1)
        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)
            self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)
            self.couleur = (random.randint(20, 215), random.randint(20, 215), random.randint(20, 215))

        self.position = self.direction + self.position

        if clique is not None:
            self.Ux = clique - self.position
            self.l = self.Ux.length()
            self.Ux = self.Ux.normalize()
            self.L = abs(self.l - self.l0)
            self.direction = self.direction + self.Fx

        else:
            self.Ux = Vector2(0, 0)

        self.Fx = 0.0004 * self.L * self.Ux
        if self.direction.length() > self.vitesseMax and self.direction.length() != 0:
            self.direction = self.direction.normalize()
            self.direction.scale_to_length(self.vitesseMax)

        self.position = self.direction + self.position

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
