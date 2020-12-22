def latest(scores):
    """Return the last score of the player"""
    return scores[-1]


def personal_best(scores):
    """Return the High score of the player"""
    return max(scores)


def personal_top_three(scores):
    """Return the top three scores of a player."""
    return sorted(scores, reverse=True)[:3]
