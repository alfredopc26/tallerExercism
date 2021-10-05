from math import sqrt


def score(x: float, y: float) -> int:  # pylint: disable=invalid-name
    """
    Given a landing point for a dart, return the score earned.
    """
    distance = sqrt(x * x + y * y)
    if distance > 10:
        return 0
    if distance > 5:
        return 1
    if distance > 1:
        return 5
    return 10