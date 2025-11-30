import pygame
import os

class Pet:
    def __init__(self):
        self.state = "idle"
        self.animations = {
            "hello": self.load_frames("sprites/hello/"),
            "idle": self.load_frames("sprites/idle/"),
            "eat": self.load_frames("sprites/sad/"),
            "sad": self.load_frames("sprites/sad/"),
            "happy": self.load_frames("sprites/happy/"), 
        }
        self.animSpeed = { 
            "hello":400, 
            "idle": 400,
            "eat": 150,
            "sad":150,
            "happy": 200
        }
        self.current_frame = 0
        self.frame_timer = 0

    def load_frames(self, folder):
        frames = []
        SPRITE_SIZE = (195, 197)
        for file in sorted(os.listdir(folder)):
            if file.lower().endswith(".png"):
                img = pygame.image.load(os.path.join(folder, file))
                img = pygame.transform.smoothscale(img, SPRITE_SIZE)
                frames.append(img)
        return frames

    def update(self, dt):
        self.frame_timer += dt
        speed = self.animSpeed.get(self.state, 150)
        frames = self.animations[self.state]

        if self.frame_timer > speed:
            self.frame_timer = 0
            # default animtation: Idle loops forever. When a button is clicked does the other animation 1 time
            #Todo: click queue but in main or tamagotchi
            if self.state == "idle":
                self.current_frame = (self.current_frame + 1) % len(frames)
            else:
                if self.current_frame < len(frames) - 1:
                    self.current_frame += 1
                else:
                    self.state = "idle"
                    self.current_frame = 0

    def draw(self, screen):
        frame = self.animations[self.state][self.current_frame]
        screen.blit(frame, (200, 200))
