from configparser import ConfigParser
import pygame
import random
from os import getcwd

from particle import Particle, particles

path = getcwd()

if __name__ == "__main__":
    # Load Config
    defaults = ConfigParser()
    defaults.read(f"{path}\\defaults.ini")
    
    # Initialise Variables
    screenWidth  = int(defaults['screen']['width'])
    screenHeight = int(defaults['screen']['height'])
    FPS          = int(defaults['screen']['FPS'])
    aspectRatio  = screenWidth / screenHeight

    # Initialise Screen
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("Physics Simulation")
    clock = pygame.time.Clock()
    
    # Spawn Particles
    length = 16
    for x in range(length):
        for y in range(length):
            spawnX = x * (screenHeight / length) + ((screenWidth - screenHeight) / 2)
            spawnY = y * (screenHeight / length)
            
            particles.add(
                Particle(spawnX, spawnY, random.randint(1, 100), 5, (255, 255, 255))
            )
    
    # Main Loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.fill((0, 0, 0))
        
        # Simulate Particles
        for particle in particles:
            particle.move()
        for particle in particles:
            particle.update()
            particle.draw(screen)
        
        pygame.display.update()
        clock.tick(FPS)
            
pygame.quit()
exit()