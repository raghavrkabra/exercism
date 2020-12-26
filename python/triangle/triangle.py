def equilateral(sides: list) -> bool:
    triangle = sorted(sides)

    if triangle[0] == 0:
        return False

    return len(set(sides)) == 1


def isosceles(sides: list) -> bool:
    triangle = sorted(sides)

    if triangle[0] == 0:
        return False

    if triangle[0] == triangle[1] or triangle[1] == triangle[2]:
        return triangle[0] + triangle[1] >= triangle[2]

    return False


def scalene(sides: list) -> bool:
    triangle = sorted(sides)

    if triangle[0] == 0:
        return False

    if len(set(triangle)) == 3:
        return triangle[0] + triangle[1] >= triangle[2]

    return False
