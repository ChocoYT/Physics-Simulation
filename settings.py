'''
This file contains the settings for a quantum particle simulation.
'''

class Screen:
    width = 1000
    height = 800
    FPS = 60

class Constants:
    G = 0.980665
    K = 8.99

class Quarks:
    class Up:
        mass = 3.56
        size = 4
        colour = 255, 0, 0
        
    class Down:
        mass = 8.9
        size = 4
        colour = 0, 255, 0
        
class Leptons:
    class Electron:
        mass = 0.91093837
        size = 2
        colour = 80, 150, 255