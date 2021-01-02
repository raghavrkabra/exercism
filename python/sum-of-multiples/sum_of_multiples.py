def sum_of_multiples(limit: int, factors: list) -> int:
    """Give sum of all the multiples of given numbers untill given limit"""
    set_of_multiples = {i
                        for factor in factors
                        if factor != 0
                        for i in range(factor, limit, factor)
                        }
    return sum(set_of_multiples)
