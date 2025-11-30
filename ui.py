import pygame

class Button:
    def __init__(self, x, y, width, height, text, color=(180, 180, 180)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
       
def stat_bar(screen, x, y, w, h, percent, color):
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w, h)) 
    pygame.draw.rect(screen, color, (x, y, w * (percent / 100), h))  
