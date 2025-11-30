import pygame
from pet import Pet
from ui import Button, stat_bar
from mechanic import Mechanics

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

pet = Pet()
mechanics = Mechanics()

bg_color = (255, 220, 180)  

eat_button = Button(50, 500, 150, 50, "EAT")
cuddle_button = Button(225, 500, 150, 50, "CUDDLE")
play_button = Button(400, 500, 150, 50, "PLAY")


running = True
while running:
    dt = clock.tick(60)
    mechanics.update(dt)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if eat_button.is_clicked(pos):
                mechanics.feed()
                pet.state = "eat"
            elif cuddle_button.is_clicked(pos):
                mechanics.cuddle()
                pet.state = "happy"
            elif play_button.is_clicked(pos):
                mechanics.play()
                pet.state = "play"

    screen.fill(bg_color)

    pet.update(dt)
    pet.draw(screen)

    eat_button.draw(screen)
    cuddle_button.draw(screen)
    play_button.draw(screen)
    
    stat_bar(screen, 50, 50, 200, 20, mechanics.hunger, (200, 50, 50))
    stat_bar(screen, 50, 80, 200, 20, mechanics.happiness, (50, 200, 50))
    stat_bar(screen, 50, 110, 200, 20, mechanics.energy, (50, 50, 200))


    pygame.display.update()

pygame.quit()
