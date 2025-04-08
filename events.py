import pygame

class Events:
    def __init__(self):
        self._mousePosition = pygame.Vector2(pygame.mouse.get_pos())
        self._mouseButtons  = pygame.mouse.get_pressed()
        self._keysPressed   = pygame.key.get_pressed()
        
        self._oldMousePosition = self._mousePosition
        self._oldMouseButtons  = self._mouseButtons
        self._oldkeysPressed   = self._keysPressed
        
    def getMousePosition(self) -> pygame.Vector2:  return self._mousePosition
    def getMouseMovement(self) -> pygame.Vector2:  return self._mousePosition - self._oldMousePosition
    
    def isMouseButtonPressed(self,  button: int) -> bool: return self._mouseButtons[button] and not self._oldMouseButtons[button]
    def isMouseButtonReleased(self, button: int) -> bool: return not self._mouseButtons[button] and self._oldMouseButtons[button]
    
    def isKeyPressed(self,  key: int) -> bool: return self._keysPressed[key] and not self._oldkeysPressed[key]
    def isKeyReleased(self, key: int) -> bool: return not self._keysPressed[key] and self._oldkeysPressed[key]
        
    def update(self, events = None) -> None:
        self._oldMousePosition = self._mousePosition
        self._oldMouseButtons  = self._mouseButtons
        self._oldkeysPressed   = self._keysPressed
        
        if events is None:  return
        
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                self._mousePosition = pygame.Vector2(event.pos)
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self._mouseButtons = pygame.mouse.get_pressed()
                
                if event.button == pygame.K_ESCAPE:  self.quit()
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                self._keysPressed = pygame.key.get_pressed()

            if event.type == pygame.QUIT:  self.quit()
        
    def quit(self) -> None:
        pygame.quit()
        exit()