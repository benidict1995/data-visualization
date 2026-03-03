from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialized attributes"""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """"Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:

            # Decide which direction to go.
            x_step = self.direction()
            y_step = self.direction()

            # Reject moves
            if y_step == 0 and x_step == 0:
                continue

            # New position
            self.x_values.append(self.x_values[-1] + x_step)
            self.y_values.append(self.y_values[-1] + y_step)

    def direction(self):
        """X direction"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance