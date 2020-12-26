def equilateral(sides: list) -> bool:
    """Return True if given sides form a equilateral traiangle."""
    if _is_triangle(sides):
        return len(set(sides)) == 1

    return False


def isosceles(sides: list) -> bool:
    """Return True if given sides form a isosceles traiangle."""
    if _is_triangle(sides):
        return len(set(sides)) <= 2

    return False


def scalene(sides: list) -> bool:
    """Return True if given sides form a scalene traiangle."""
    if _is_triangle(sides):
        return len(set(sides)) == 3

    return False


def _is_triangle(sides:list) -> bool:
    """Return True if given sides form a traiangle."""
    if 0 in sides:
        return False

    return sum(sides) >= 2*max(sides)
