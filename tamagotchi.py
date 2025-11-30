import pygame
from pet import Pet

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

pet = Pet()

# start color (dark grey)
bg_color = (255, 220, 180)  

running = True
while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(bg_color)

    # Update + draw pet
    pet.update(dt)
    pet.draw(screen)

    pygame.display.update()

pygame.quit()
