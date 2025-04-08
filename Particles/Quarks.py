import pygame

from particle import Particle
from settings import *

class Up(Particle):
    def __init__(self, position: pygame.Vector2) -> None:
        super().__init__(position.x, position.y, Quarks.Up.mass, Quarks.Up.size, Quarks.Up.colour)
        
        self.charge = 2
        
class Down(Particle):
    def __init__(self, position: pygame.Vector2) -> None:
        super().__init__(position.x, position.y, Quarks.Down.mass, Quarks.Down.size, Quarks.Down.colour)
        
        self.charge = 1