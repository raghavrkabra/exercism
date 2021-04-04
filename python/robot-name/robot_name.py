from random import choices
from string import ascii_uppercase, digits


class Robot:
    """Robot factory to create and reset them."""

    robot_population = set()

    def __init__(self):
        self.name = self.create_robot()

    def _generate_name(self):
        """Create a valid robot name."""
        return "".join(choices(ascii_uppercase, k=2) + choices(digits, k=3))

    def create_robot(self):
        """Create a robot and ensure it's name is unique."""
        name = self._generate_name()
        while name in self.robot_population:
            name = self._generate_name()
        self.robot_population.add(name)
        return name

    def reset(self):
        """Reset a robot and give it a new new name."""
        self.name = self.create_robot()
