import pygame
class Mechanics:
    def __init__(self, debug=True):
        self.hunger = 200.0
        self.happiness = 100.0
        self.energy = 100.0

        self.debug = debug

        self.actions = {
            "eat":     {"hunger": +20, "happiness": +5},
            "cuddle":  {"happiness": +15},
            "play":    {"energy": -10, "happiness": +10},
        }

    def _clamp(self, value):
        return max(0, min(100, value))

    def _print_stats(self, prefix=""):
        if not self.debug:
            return
        print(
            f"{prefix}"
            f"Hunger: {self.hunger:6.2f} | "
            f"Energy: {self.energy:6.2f} | "
            f"Happiness: {self.happiness:6.2f}"
        )

    def apply_action(self, action_name):
        if action_name not in self.actions:
            return

        if self.debug:
            print(f"\n▶ Action: {action_name.upper()}")

        for stat, change in self.actions[action_name].items():
            old = getattr(self, stat)
            new = self._clamp(old + change)
            setattr(self, stat, new)

            if self.debug:
                print(f"  {stat}: {old:.2f} → {new:.2f}")

        self._print_stats("  → ")

    def update(self, dt):
        """Called every frame — decrease stats over time."""
        seconds = dt / 10.0

        decay = {
            "hunger": 0.1,
            "energy": 0.05,
            "happiness": 0.02,
        }

        changed = False

        for stat, rate in decay.items():
            old = getattr(self, stat)
            new = self._clamp(old - rate * seconds)
            if new != old:
                setattr(self, stat, new)
                changed = True

        # Print once per second (prevents spam)
        if self.debug and int(pygame.time.get_ticks() / 100000) % 1 == 0 and changed:
            self._print_stats("[Tick] ")
