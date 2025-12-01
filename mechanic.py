class Mechanics:
    def __init__(self):
        self.hunger = 100
        self.happiness = 100
        self.energy = 100

        self.actions = {
            "eat":     {"hunger": +20, "happiness": +5},
            "cuddle":  {"happiness": +15},
            "play":    {"energy": -10, "happiness": +10},
        }

    def apply_action(self, action_name):
        if action_name not in self.actions:
            return
        
        for stat, change in self.actions[action_name].items():
            value = getattr(self, stat)
            setattr(self, stat, max(0, min(100, value + change)))

    def update(self, dt):
        """Called every frame — decrease stats over time."""
        self.hunger = max(0, self.hunger - 0.1 * dt)
        self.energy = max(0, self.energy - 0.05 * dt)
        self.happiness = max(0, self.happiness - 0.02 * dt)
