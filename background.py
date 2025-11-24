import pygame

class BackgroundManager:
    def __init__(self):
        self.backgrounds = {
            "inside": pygame.image.load("assets/sprites/backgrounds/inside.png"),
            "outside": pygame.image.load("assets/sprites/backgrounds/outside.png"),
        }
        self.current = "inside"

    def switch(self, name):
        if name in self.backgrounds:
            self.current = name

    def draw(self, screen):
        screen.blit(self.backgrounds[self.current], (0, 0))
