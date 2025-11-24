import pygame

class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen):
        text = self.font.render("Press SPACE to start", True, (255, 255, 255))
        screen.blit(text, (150, 200))
