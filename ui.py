import pygame
from pygame_gui.core import ObjectID
from pygame_gui.elements import UIButton, UIWindow

def create_action_button(manager, text, pos, size=(150, 50)):
    return UIButton(
        relative_rect=pygame.Rect(pos, size),
        text=text,
        manager=manager,
        object_id=ObjectID(class_id='@action_buttons', object_id=f'#{text.lower()}_button')
    )

def create_window(manager):
    return UIWindow(
        rect=pygame.Rect((100, 100), (600, 400)),
        manager=manager,
        window_display_title="My Tamagotchi"
    )
