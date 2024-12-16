import pygame

G = 1

class Particle():
    def __init__(self, x: int,  y: int, mass: float, size: int, colour: tuple[int]) -> None:
        self.x, self.y = x, y
        self.pos = self.x, self.y
        self.xVel, self.yVel = 0, 0
        
        self.mass = mass
        
        self.size = size
        self.radius = self.size / 2
        self.colour = colour
        
        self.image = pygame.Surface((self.size, self.size))
        pygame.draw.circle(self.image, self.colour, (self.radius, self.radius), self.radius)
        self.image.set_colorkey((0, 0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        
    def move(self) -> None:
        for particle in particles:
            if not self is particle:
                xDist = particle.rect.x - self.x
                yDist = particle.rect.y - self.y
                dist = ((xDist ** 2) + (yDist ** 2)) ** 0.5
                
                if dist > 1:
                    xDist /= dist
                    yDist /= dist
                
                    force = (G * self.mass * particle.mass) / (dist ** 2)

                    self.xVel += (force / self.mass) * xDist
                    self.yVel += (force / self.mass) * yDist
        
        self.x += self.xVel
        self.y += self.yVel
        
    def update(self) -> None:
        self.pos = self.x, self.y
        self.rect.topleft = self.pos
    
    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect.center)
        
particles = set()