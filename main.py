import pygame
from pet import Pet
from mechanic import Mechanics
from background import BackgroundManager
from menu import Menu

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

pet = Pet()
mechanics = Mechanics()
bg = BackgroundManager()
menu = Menu()

running = True
in_menu = True

while running:
    dt = clock.tick(60)  # milliseconds passed since last frame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if in_menu and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                in_menu = False

    if in_menu:
        menu.draw(screen)
    else:
        mechanics.update(dt)
        pet.update(dt)
        bg.draw(screen)
        pet.draw(screen)

    pygame.display.flip()

pygame.quit()
