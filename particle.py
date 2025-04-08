import pygame

from settings import *

class Particle:
    def __init__(self, x: int,  y: int, mass: float, size: int, colour: tuple[int]) -> None:
        self.x, self.y = x, y
        self.xVel, self.yVel = 0, 0
        
        self.mass = mass
        
        self.size = size
        self.radius = self.size / 2
        self.colour = colour
        
        self.image = pygame.Surface((self.size, self.size))
        pygame.draw.circle(self.image, self.colour, (self.radius, self.radius), self.radius)
        self.image.set_colorkey((0, 0, 0))
        
        self.rect = self.image.get_rect()
        
        self.update()
        
        particles.add(self)
        
    def move(self) -> None:
        for particle in particles:
            if not self is particle:
                
                dist = pygame.Vector2(particle.x, particle.y) - pygame.Vector2(self.x, self.y)
                
                if dist.x == 0 and dist.y == 0:  continue
                
                normalisedDist = dist.normalize()
                magnitude      = dist.magnitude()
                
                # Apply Gravity
                if magnitude >= 1:
                    force = Constants.G * particle.mass / dist.magnitude_squared()

                    self.xVel += force * normalisedDist.x
                    self.yVel += force * normalisedDist.y
                            
        self.x += self.xVel
        self.y += self.yVel
        
    def update(self) -> None:
        self.rect.center = self.x, self.y
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect.topleft)
        
particles: set[Particle] = set()