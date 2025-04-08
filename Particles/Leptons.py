import pygame

from particle import Particle
from settings import *

class Electron(Particle):
    def __init__(self, position: pygame.Vector2) -> None:
        super().__init__(position.x, position.y, Leptons.Electron.mass, Leptons.Electron.size, Leptons.Electron.colour)
        
        self.charge = -3