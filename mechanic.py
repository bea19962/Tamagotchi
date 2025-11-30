class Mechanics:
    def __init__(self):
        # Initial stats
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

        # Speed of change per second
        self.hunger_rate = 5    # hunger increases 5 per second
        self.happiness_rate = 2 # happiness decreases 2 per second

    def update(self, dt):
        """Update stats based on time passed"""
        seconds = dt / 1000  # dt is in milliseconds
        self.hunger += self.hunger_rate * seconds
        self.happiness -= self.happiness_rate * seconds

        # Clamp stats between 0 and 100
        self.hunger = min(100, max(0, self.hunger))
        self.happiness = min(100, max(0, self.happiness))

    # Interaction methods
    def feed(self):
        self.hunger -= 20
        self.hunger = max(0, self.hunger)

    def cuddle(self):
        self.happiness += 15
        self.happiness = min(100, self.happiness)

    def play(self):
        self.happiness += 20
        self.energy -= 10
        self.energy = max(0, self.energy)
        self.happiness = min(100, self.happiness)
