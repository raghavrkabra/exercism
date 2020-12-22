from random import choices
from string import ascii_uppercase, digits


def _generate_name():
    """Create a valid robot name."""
    return "".join(choices(ascii_uppercase, k=2) + choices(digits, k=3))

class Robot:
    """Robot factory to create and reset them."""
    def __init__(self):
        self.name = self.create_robot()

    robot_population = set()

    def create_robot(self):
        """Create a robot and ensure it's name is unique."""
        name_ = _generate_name()
        while name_ in self.robot_population:
            name_ = _generate_name()
        self.robot_population.add(name_)
        return name_

    def reset(self):
        """Reset a robot and give it a new new name."""
        old_name = self.name
        self.name = self.create_robot()
        self.robot_population.remove(old_name)
