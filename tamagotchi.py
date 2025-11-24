import pygame
import time

pygame.init()

# Window
WIDTH, HEIGHT = 400, 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Tamagotchi")

# Load sprites
idle = pygame.image.load("sprites/idle.png")
happy = pygame.image.load("sprites/happy.png")
hungry = pygame.image.load("sprites/hungry.png")

# Stats
hunger = 50
happiness = 50
last_update = time.time()

state = "idle"


def update_stats():
    global hunger, happiness, last_update, state

    # Decrease stats every few seconds
    if time.time() - last_update > 3:
        hunger += 5
        happiness -= 2
        last_update = time.time()

    # Clamp values
    hunger = min(100, max(0, hunger))
    happiness = min(100, max(0, happiness))

    # Determine state
    if hunger > 70:
        state = "hungry"
    elif happiness > 70:
        state = "happy"
    else:
        state = "idle"


def draw():
    window.fill((30, 30, 30))

    if state == "idle":
        window.blit(idle, (100, 100))
    elif state == "happy":
        window.blit(happy, (100, 100))
    elif state == "hungry":
        window.blit(hungry, (100, 100))

    pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Interactions: FEED when pressing F, PLAY when pressing P
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # feed
                hunger -= 20
            if event.key == pygame.K_p:  # play
                happiness += 20

    update_stats()
    draw()

pygame.quit()
