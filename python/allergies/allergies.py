"""Solution to Allergies exercies in python track on exercism."""


class Allergies:
    """This class keep track of allergies of the person."""

    _allergies = [
            "eggs",
            "peanuts",
            "shellfish",
            "strawberries",
            "tomatoes",
            "chocolate",
            "pollen",
            "cats"
            ]

    def __init__(self, score: int) -> None:
        self.score = score

    def allergic_to(self, item: str) -> bool:
        """Check to see if a person is allergiec to given item."""
        return bool(self.score & 1 << self._allergies.index(item))

    @property
    def lst(self) -> list:
        """Turn given allergy code into a list of allergies."""
        return [allergy for allergy in self._allergies
                if self.allergic_to(allergy)]
