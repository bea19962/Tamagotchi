class Mechanics:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.energy = 70

    def update(self, dt):
        self.hunger += 0.01 * dt
        self.happiness -= 0.02 * dt

        self.hunger = min(100, max(0, self.hunger))
        self.happiness = min(100, max(0, self.happiness))
