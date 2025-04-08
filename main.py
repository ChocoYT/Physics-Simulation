import pygame

from events import Events
from particle import particles
from settings import *

from Particles import Quarks, Leptons

pygame.init()

if __name__ == "__main__":

    # Initialise Screen
    screen = pygame.display.set_mode((Screen.width, Screen.height))
    pygame.display.set_caption("Physics Simulation")
    clock = pygame.time.Clock()
    
    mousePosition = pygame.Vector2(pygame.mouse.get_pos())
    mouseButton = pygame.mouse.get_pressed()
    
    events = Events()
    
    # Main Loop
    while True:
        screen.fill((0, 0, 0))
        
        mousePosition = events.getMousePosition()
        
        if events.isMouseButtonPressed(0):
            Quarks.Up(mousePosition)
        if events.isMouseButtonPressed(1):
            Leptons.Electron(mousePosition)
        if events.isMouseButtonPressed(2):
            Quarks.Down(mousePosition)
        
        # Simulate Particles
        for particle in particles:
            particle.move()
        for particle in particles:
            particle.update()
            particle.draw(screen)
            
        events.update(pygame.event.get())
        
        pygame.display.update()
        clock.tick(Screen.FPS)
