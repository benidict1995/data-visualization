from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume six sides."""
        self.num_sides = num_sides

    def roll(self):
        """Simulate rolling the die."""
        return randint(1, self.num_sides)