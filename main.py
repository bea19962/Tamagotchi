import asyncio
import pygame
import pygame_gui
from pet import Pet
from ui import create_action_button, create_status_bar
from mechanic import Mechanics
import json

with open("theme.json", "r") as f:
    theme = json.load(f)


async def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tamagotchi")
    clock = pygame.time.Clock()

    # --- UI Manager ---
    manager = pygame_gui.UIManager((800, 600), 'theme.json')
    manager.set_visual_debug_mode(True)
    
    
    mechanics = Mechanics()
    actions_buttons = {}
    x, y = 150, 500
    gap = 25
    for action_name in mechanics.actions.keys():
        actions_buttons[action_name] = create_action_button(manager, action_name.capitalize(), (x, y))
        x += 150 + gap
        
    # --- Status bars ---
    hunger_bar = create_status_bar(manager, "hunger")
    # --- Game objects ---
    pet = Pet()
   #bg_color = theme["defaults"]["colours"]["norml_bg"]
    bg_color = "#ffffff"

    running = True
    while running:
        dt = clock.tick(60)
        time_delta = dt / 1000.0  # convert to seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                for action_name, button in actions_buttons.items():
                    if event.ui_element == button:
                        mechanics.apply_action(action_name)
                        pet.state = action_name
                        print(f"Action performed: {action_name}, points: {mechanics.actions[action_name]}")


        # --- Update ---
        mechanics.update(dt)
        pet.update(dt)
        manager.update(time_delta)
        
        # --- Update status bars ---
        hunger_bar.set_current_progress(mechanics.hunger / 100)



        # --- Draw ---
        screen.fill(bg_color)
        pet.draw(screen)
        manager.draw_ui(screen)

        pygame.display.update()
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())
