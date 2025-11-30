import pygame

class Pet:
    def __init__(self):
        self.state = "idle"
        self.animations = {
            "idle": self.load_frames("assets/sprites/idle 1/"),
            "eat": self.load_frames("assets/sprites/Happy 2/")
        }
        self.current_frame = 0
        self.frame_timer = 0

    def load_frames(self, folder):
        import os
        frames = []
        for file in sorted(os.listdir(folder)):
            if file.endswith(".png"):
                frames.append(pygame.image.load(folder + file))
        return frames

    def update(self, dt):
        # handle animation timing
        self.frame_timer += dt
        if self.frame_timer > 150:  # every 150 ms
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.state])
            self.frame_timer = 0

    def draw(self, screen):
        frame = self.animations[self.state][self.current_frame]
        screen.blit(frame, (200, 200))
