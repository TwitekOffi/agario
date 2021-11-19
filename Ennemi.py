import random
import pygame
from pygame.math import Vector2
import core


class Ennemi:
    def __init__(self):
        self.vitesseMax = 8
        self.position = Vector2(random.randint(0, 1075), random.randint(0, 715))
        self.couleur = (random.randint(150, 255), 0, 0)
        self.rayon = 5
        self.nom = "Test"
        self.ChampsDeVision = 75
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

    def deplacer(self,h,l):

        # DEPLACEMENT RANDOM
        self.Fx = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.direction = self.direction + self.Fx
        self.position = self.direction + self.position
        if self.position.x < 0 or self.position.x > l:
            self.direction = Vector2(self.direction.x * -1, self.direction.y)

        if self.position.y < 0 or self.position.y > h:
            self.direction = Vector2(self.direction.x, self.direction.y * -1)

        if self.direction.length() > self.vitesseMax and self.direction.length() != 0:
            self.direction = self.direction.normalize()
            self.direction.scale_to_length(self.vitesseMax)

    def perception(self):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)
